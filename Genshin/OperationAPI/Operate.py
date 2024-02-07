#这里写模拟用户玩游戏的操作,比如键盘事件,鼠标事件
#由于这个需要管理员权限,不是管理员权限将自动给与
import ctypes
from User import MYMouse as Mouse
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
    
    def mouse(self,button=Mouse.NotAnyOperation,x: int=0,y: int=0):
        width = self.user32.GetSystemMetrics(0)
        height = self.user32.GetSystemMetrics(1)
        absolute_x = 65536 * x // width + 1
        absolute_y = 65536 * y // height + 1
        if button == Mouse.Left_down:
            self.mouse_event(Mouse.Left_down | Mouse.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)
        elif button == Mouse.Left_up:
            self.mouse_event(Mouse.Left_up | Mouse.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)
        elif button == Mouse.Right_down:
            self.mouse_event(Mouse.Right_down | Mouse.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)
        elif button == Mouse.Right_up:
            self.mouse_event(Mouse.Right_up | Mouse.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)
        elif button == Mouse.Middle_down:
            self.mouse_event(Mouse.Middle_down | Mouse.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)
        elif button == Mouse.Middle_up:
            self.mouse_event(Mouse.Middle_up | Mouse.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)
        elif button == Mouse.Move:
            self.mouse_event(Mouse.Move | Mouse.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)
        elif button == Mouse.NotAnyOperation:
            pass
        else:
            raise ValueError("Unknown mouse operation")

operation = Operate()