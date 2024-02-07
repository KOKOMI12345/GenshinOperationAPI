import time
from Operate import operation
import User
from Log4p import LogManager
Logmanager = LogManager()
#定义原神角色操作的类
class CharacterOperation:
    """
    角色操作API类
    """
    def __init__(self,name: str = None,noWarning: bool = False):
        self.log = Logmanager.GetLogger("角色操作日志")
        self.name = name
        self.log.info(f"角色操作类初始化,角色为 {self.name} 正在使用此操控器")
        self.noWarning = noWarning
        pass

    def Jump(self,chance: int = 1):
        
        for i in range(chance):
           operation.press_key(User.Keyboard.SPACE)
           operation.release_key(User.Keyboard.SPACE)
           time.sleep(1)
        self.log.info("跳跃")

    def MouseLeftClick(self):
        operation.mouse(User.Mouse.MOUSEEVENT_LEFTDOWN,0,0)
        operation.mouse(User.Mouse.MOUSEEVENT_LEFTUP)
    def MoveMouseToPosition(self,x=None,y=None):
        operation.mouse(1,x,y)
        self.log.info(f"移动鼠标到坐标({x},{y})")

    def Forward(self,times):
        operation.press_key(User.Keyboard.W)
        time.sleep(times)
        operation.release_key(User.Keyboard.W)
        self.log.info("向前移动")

    def Backward(self,times):
        operation.press_key(User.Keyboard.S)
        time.sleep(times)
        operation.release_key(User.Keyboard.S)
        self.log.info("向后移动")

    def Left(self,times):
        operation.press_key(User.Keyboard.A)
        time.sleep(times)
        operation.release_key(User.Keyboard.A)
        self.log.info("向左移动")

    def Right(self,times):
        operation.press_key(User.Keyboard.D)
        time.sleep(times)
        operation.release_key(User.Keyboard.D)
        self.log.info("向右移动")
        
    def CheckPramater(self,times: float = 1.0):
        if self.noWarning == False:
          self.log.warning("这个方法有点问题,我用了给我鼠标和输入法搞没了,等了好一会才好")
          self.log.warning("不知道你们会不会有类似的问题")
        operation.mouse(User.Mouse.MOUSECENTERKEY_UP)
        time.sleep(times)
        operation.mouse(User.Mouse.MOUSECENTERKEY_DOWN)

    def Fire(self,method: str = None,timer:float = None):  
        if method == 'Normal':
            operation.mouse(User.Mouse.MOUSEEVENT_LEFTUP)
            if timer == None:
                timer = 0.5
                time.sleep(timer)
            operation.mouse(User.Mouse.MOUSEEVENT_LEFTDOWN)
            self.log.info(f"普通攻击,间隔{timer}秒")
        elif method == 'Charged':
          if timer == None:
              timer = 0.5
          operation.press_key(User.Keyboard.E)
          time.sleep(timer)
          operation.release_key(User.Keyboard.E)
          self.log.info(f"蓄力攻击,蓄力{timer}秒")
        elif method == "Skill":
          operation.press_key(User.Keyboard.Q)
          time.sleep(0.5)
          operation.release_key(User.Keyboard.Q)
          self.log.info(f"{self.name}发动大招")
        elif method == "Quickly":
            if (self.name != "娜维娅" or self.name != "navia" or self.name != "Navia") and self.noWarning == False:                
                self.log.warning(f"警告:该角色不是纳维娅,这个攻击方法是专门为娜维娅设计的,可能体验不佳,如果你不想接收到类似警告,请把noWarning改为False")
            for a in range(3):
                operation.press_key(User.Keyboard.E)
                operation.release_key(User.Keyboard.E)
                time.sleep(0.8)
              
        elif method == "TurnedATK":
            operation.mouse(User.Mouse.MOUSEEVENT_LEFTDOWN)
            time.sleep(timer)
            operation.mouse(User.Mouse.MOUSEEVENT_LEFTUP)
        elif method == "Drop":
            operation.mouse(User.Mouse.MOUSEEVENT_LEFTDOWN)
            operation.mouse(User.Mouse.MOUSEEVENT_LEFTUP)

    def pick_item(self):
        operation.press_key(User.Keyboard.F)
        operation.release_key(User.Keyboard.F)