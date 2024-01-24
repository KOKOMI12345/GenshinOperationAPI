#这里写模拟用户玩游戏的操作,比如键盘事件,鼠标事件
#由于这个需要管理员权限,不是管理员权限将自动给与
import ctypes
class Operate:
    """
    最底层的实现API类
    """
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.keybd_event = ctypes.windll.user32.keybd_event
        self.mouse_event = ctypes.windll.user32.mouse_event

    def press_key(self, key=None):
        self.keybd_event(key, 0, 0, 0)

    def release_key(self, key=None):
        self.keybd_event(key, 0, 2, 0)
    
    def mouse(self,button=0x0001,x: int=0,y: int=0):
        #这里写移动鼠标的逻辑
        self.user32.SetProcessDPIAware()
        width, height = self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)
        dx = int(x * 65535 / width)
        dy = int(y * 65535 / height)
        self.mouse_event(button, dx, dy, 0, 0)

operation = Operate()