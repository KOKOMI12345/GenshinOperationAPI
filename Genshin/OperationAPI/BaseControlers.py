#这里写自己要操控角色的逻辑
from dependent import *

class BaseControlers:
    def __init__(self,name:str = None):
        self.name = f"{name}"
        self.log = config_log(log_name="控制器")
        self.characteroperation = CharacterOperation(self.name)

    def Fire(self,method: str = None,times:float = None,change : int = None,timeWait : float = None):
        """
        `method: 攻击方法
        `times: 每次攻击的间隔,如果攻击模式为Charged,这个就代表蓄力时间(max:5)
        `change: 攻击次数
        `timeWait: 每次攻击完成后下一次攻击的时间间隔
        """
        self.log.info(f"{self.name}发动了攻击！")
        change = change
        timeWait = timeWait
        self.log.info(f"{self.name}将使用{method}方法,攻击{change}次")
        for i in range(change):
            self.characteroperation.Fire(method,times)
            time.sleep(timeWait)
        self.log.info(f"{self.name}攻击完成！")
        return True
    
    def Operate(self):
     """
     NOTE: 下面是示例调用代码
     """
     try:
        self.log.info(f"{self.name}发动了操作！")
        self.characteroperation.Forward(6)
        self.log.info(f"{self.name}操作完成！")
        return True
     except Exception as e:
        self.log.warning(f"{self.name}操作失败！")
        self.log.exception(e)
        return False
    
    def quickly_shooting(self):
        # 在这里编写娜维娅的逻辑
        self.log.info(f"{self.name}发动了快速射击！")
        self.characteroperation.Fire(method="Quickly")
        self.log.info(f"{self.name}快速射击完成！")
        return True
    #连点器
    def ReclickQuick(self,chance:int = 1):
        for _ in range(chance):
           self.characteroperation.MouseLeftClick()
           time.sleep(0.1)