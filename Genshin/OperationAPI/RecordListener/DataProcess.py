from RecordListener.eventConst import MYKeyboard as Keyboard , MYMouse as Mouse
"""
把json中的特殊按键转换为对应的十六进制键值
"""

class TransformerToVal:
    def __init__(self):
        pass

    def TranslateKey(self,key:str = None):
       clean_key = key.strip("'")
       try:
         value = getattr(Keyboard,clean_key.upper())
         return value
       except:
        if clean_key == "Key.space":
           return Keyboard.SPACE
        elif clean_key == "key.shift":
           return Keyboard.SHIFT
        elif clean_key == "key.ctrl":
           return Keyboard.CONTROL
        elif clean_key == "key.alt":
           return Keyboard.ALT
        elif clean_key == "key.tab":
           return Keyboard.TAB
        elif clean_key == "key.enter":
           return Keyboard.ENTER
        elif clean_key == "key.backspace":
           return Keyboard.BACKSPACE
        elif clean_key == "key.delete":
           return Keyboard.DELETE
        elif clean_key == "?":
           return Keyboard.UNKNOWN
        elif clean_key == ",":
           return Keyboard.COMMA
        elif clean_key == "!":
           return Keyboard.EXCLAMATION
        elif clean_key == ")":
           return Keyboard.RIGHT_PARENTHESIS
        elif clean_key == "(":
           return Keyboard.LEFT_PARENTHESIS
        elif clean_key == ".":
           return Keyboard.PERIOD
        elif clean_key == "'":
           return Keyboard.APOSTROPHE
        elif clean_key == ";":
           return Keyboard.SEMICOLON
        elif clean_key == ":":
           return Keyboard.COLON
        elif clean_key == "/":
           return Keyboard.SLASH
        else:
           pass
    
    def TranslateMouse(self,mouse:str = None):
        return getattr(Mouse,mouse)

translate = TransformerToVal()
