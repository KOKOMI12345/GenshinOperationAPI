import ctypes
from RecordListener import Listener
import sys
class Admin:
    def __init__(self):
        pass

    def RunThread(self,func):
        if ctypes.windll.shell32.IsUserAnAdmin():
            self.log.info("当前用户是管理员权限")
            func()
        else:
            self.log.info("当前用户不是管理员权限，正在尝试获取管理员权限")
            # 获取管理员权限
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

if __name__ == '__main__':
    admin = Admin()
    listener = Listener.Listener()
    funcs = listener.start
    admin.RunThread(funcs)