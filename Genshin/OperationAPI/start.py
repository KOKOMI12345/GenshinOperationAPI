from NaviaConntrolers import *

class FuncToNavia:
    """
    这个类是用于写攻击逻辑的实现的,
    也就是调用我写的API的地方,
    映射的操控器: NaviaConntrolers.py
    """
    def __init__(self):
        self.log = config_log("入口")
        pass

    def MainFunc(self,timeWaitToRun : float = 5):
        #示例调用
        self.log.warning(f"{timeWaitToRun}秒后开始执行,立刻切回游戏")
        time.sleep(timeWaitToRun)
        self.log.info("开始执行")
        navia.Fire(method="Charged",times=0.5,change=3,timeWait=7)
        self.log.info("执行完毕")
        pass

class Admin:
    """
    这个管理员类是为了使底层调用系统API代码生效
    关键py文件: Operate.py
    """
    def __init__(self):
        self.log = config_log("管理员")
        pass

    @fatal_analyzer
    def RunThread(self,func):
        if ctypes.windll.shell32.IsUserAnAdmin():
            self.log.info("当前用户是管理员权限")
            func()
        else:
            self.log.info("当前用户不是管理员权限，正在尝试获取管理员权限")
            # 获取管理员权限
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

func = FuncToNavia()

admin = Admin()
if __name__ == '__main__':
    admin.RunThread(func=func.MainFunc)