import logging
import colorlog
import os
import websockets
import asyncio

def config_log(log_name:str,WebLogMode:bool=False,PostUrl:str=None):
    def log_names(log_name: str):
        if log_name == "" or None:
            log_name = "default"
        return log_name
    WEBSOCKET_SERVER = f"{PostUrl}"
    # 颜色配置!
    log_color_config = {
        'DEBUG': 'blue',
        'INFO': 'cyan',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
        'RESET': 'reset'
    }

    log_folder = './main_log/track_log'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder, exist_ok=True)

    logger = logging.getLogger(f'{log_name}')

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename=f'main_log/track_log/{log_names(log_name)}.log', mode='a', encoding='utf-8')

    logger.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.INFO)

    file_formatter = logging.Formatter(
        fmt='[%(asctime)s.%(msecs)03d] |%(levelname)-8s| %(filename)s | %(funcName)s | line:%(lineno)-5d |%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_formatter = colorlog.ColoredFormatter(
        fmt='%(log_color)s[%(asctime)s.%(msecs)03d] |%(levelname)-8s| %(filename)s | %(funcName)s | line:%(lineno)d | %(message)s%(reset)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors=log_color_config
    )
    console_handler.setFormatter(console_formatter)
    file_handler.setFormatter(file_formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    console_handler.close()
    file_handler.close()

    if WebLogMode == True:
        websocket_handler = WebsocketHandler(WEBSOCKET_SERVER,enabled=True)
        websocket_handler.setLevel(logging.INFO)
        websocket_handler.setFormatter(file_formatter)
        logger.addHandler(websocket_handler)

    return logger


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



if __name__ == '__main__':
    logger = config_log(log_name='example',WebLogMode=True,PostUrl='ws://localhost:8765')
    logger.info('这是一个成功信息')
