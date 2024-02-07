from RecordListener.RecordLog import LogManager
from rich.progress import track
import json

class dataIO:
    def __init__(self,file_path):
        self.file_path = file_path
        self.logmanager = LogManager()
        self.log = self.logmanager.GetLogger('dataIO')

    def read_data(self):
     try:
        if not self.file_path:
            return None
        with open(self.file_path,'r',encoding='utf-8') as f:
            self.data = json.loads(f.read())
        return self.data
     except Exception as e:
         self.log.warning(f"读取文件失败：{e}")



class Validator:
    def __init__(self):
        self.dataio = dataIO('event.json')
        self.loads = self.dataio.read_data()
        self.LogM = LogManager()
        self.log = self.LogM.GetLogger('Validator')
    
    def validate(self):
        self.log.info('开始验证')
        require_key = ['type','key','event','time']
        require_mouse_move = ['dx','dy','type','time','event']
        require_mouse_click = ['x','y','type','time','event']
        for event in track(self.loads['event'],description='验证数据中...'):
         try:
            if event['type'] == 'keyboard':
                for key in require_key:
                    if key not in event:
                        self.log.warning(f"缺少键：{key}")
            elif event['type'] == 'mouse':
                if event['event'] == 'move':
                    for key in require_mouse_move:
                        if key not in event:
                            self.log.warning(f"缺少键：{key}")
                elif event['event'] == 'click':
                    for key in require_mouse_click:
                        if key not in event:
                            self.log.warning(f"缺少键：{key}")
            else:
                self.log.error(f"未知类型：{event['type']}")
         except Exception as e:
            self.log.exception(f"验证失败：{e}")
        self.log.info('验证完成')

vail = Validator()