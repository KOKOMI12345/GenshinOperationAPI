import logging
import colorlog
import os
import websockets
import asyncio
from logging.handlers import QueueHandler, QueueListener

class LogManager:
    def __init__(self) -> None:
        pass

    def GetLogger(self,log_name: str, WebLogMode: bool = False, PostUrl: str = None):
        def log_names(log_name: str):
            if log_name == "" or None:
                log_name = "default"
            return log_name

        WEBSOCKET_SERVER = f"{PostUrl}"
        # 颜色配置!
        log_color_config = {
            'DEBUG': 'bold_blue',
            'INFO': 'bold_cyan',
            'WARNING': 'bold_yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
            'RESET': 'reset',
            'asctime': 'green'
        }

        log_folder = f'./logs/{log_name}'
        if not os.path.exists(log_folder):
            os.makedirs(log_folder, exist_ok=True)

        logger = logging.getLogger(f'{log_name}')

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(filename=f'logs/{log_name}/{log_names(log_name)}.log', mode='a', encoding='utf-8')
        queue = asyncio.Queue()
        queue_handler = QueueHandler(queue)
        queue_listener = QueueListener(queue, file_handler)

        logger.setLevel(logging.DEBUG)
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.INFO)

        file_formatter = logging.Formatter(
            fmt='%(asctime)s.%(msecs)03d | %(levelname)-8s | %(filename)s:%(lineno)d | %(classname)s | %(funcName)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s %(asctime)s.%(msecs)03d | %(levelname)-8s | %(filename)s:%(lineno)d | %(classname)s | %(funcName)s | %(message)s %(reset)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors=log_color_config
        )
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)

        class ClassNameFilter(logging.Filter):
            def filter(self, record: logging.LogRecord) -> bool:
                record.classname = record.name.split('.')[-1]
                return True

        classname_filter = ClassNameFilter()
        logger.addFilter(classname_filter)

        if not logger.handlers:
            # 检查代码是否在异步环境中运行
            if asyncio.iscoroutinefunction(logging.Handler.emit):
                logger.addHandler(queue_handler)
                asyncio.ensure_future(queue_listener.start())
            else:
                logger.addHandler(console_handler)
                logger.addHandler(file_handler)

        console_handler.close()
        file_handler.close()

        if WebLogMode == True:
            websocket_handler = WebsocketHandler(WEBSOCKET_SERVER, enabled=True)
            websocket_handler.setLevel(logging.INFO)
            websocket_handler.setFormatter(file_formatter)
            logger.addHandler(websocket_handler)


        class WebsocketHandler(logging.Handler):
            def __init__(self, server_address, enabled=False):
                super().__init__()
                self.server_address = server_address
                self.enabled = enabled

            async def send_log(self, message):
                async with websockets.connect(self.server_address) as websocket:
                    await websocket.send(message)

            def emit(self, record):
                if self.enabled:
                    log_entry = self.format(record)
                    asyncio.create_task(self.send_log(log_entry))
        return logger


if __name__ == '__main__':
    logmanager = LogManager()
    logger = logmanager.GetLogger(log_name='example')
    logger.info('这是一个成功信息')
    logger.debug('这是一个调试信息')
    logger.critical('这是一个严重错误信息')
    logger.error('这是一个错误信息')
    logger.warning('这是一个警告信息')
