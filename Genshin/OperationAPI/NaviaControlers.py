from BaseControlers import *

class NaviaControlers:
    def __init__(self):
        self.name = f"娜维娅"
        self.log = config_log(self.name)
        self.controler = BaseControlers(self.name)

    def Fire(self):
        self.controler.Fire(method="TurnedATK", times=7, change=1, timeWait=1)
        self.log.info(f"{self.name}开火了")

    def QuicklyShooting(self):
        self.controler.quickly_shooting()
        self.log.info(f"{self.name}快速射击")

    def operation(self):
        self.controler.Operate()
        self.log.info(f"{self.name}正在操作")

navia = NaviaControlers()