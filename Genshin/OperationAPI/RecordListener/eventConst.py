from ctypes import c_uint8

class MYKeyboard:
    """
    NOTE : 键盘操作类
    """
    DELETE = c_uint8(0x2E)
    UNKNOWN = c_uint8(0x3F)
    COMMA = c_uint8(0xBC)
    EXCLAMATION = c_uint8(0x21)
    RIGHT_PARENTHESIS = c_uint8(0x29)
    LEFT_PARENTHESIS = c_uint8(0x28)
    PERIOD = c_uint8(0xBE)
    APOSTROPHE = c_uint8(0xDE)
    SEMICOLON = c_uint8(0xBA)
    COLON = c_uint8(0x3A)  # 同 SEMICOLON
    SLASH = c_uint8(0xBF)
    A = c_uint8(0x41)
    B = c_uint8(0x42)
    C = c_uint8(0x43)
    D = c_uint8(0x44)
    E = c_uint8(0x45)
    F = c_uint8(0x46)
    G = c_uint8(0x47)
    H = c_uint8(0x48)
    I = c_uint8(0x49)
    J = c_uint8(0x4A)
    K = c_uint8(0x4B)
    L = c_uint8(0x4C)
    M = c_uint8(0x4D)
    N = c_uint8(0x4E)
    O = c_uint8(0x4F)
    P = c_uint8(0x50)
    Q = c_uint8(0x51)
    R = c_uint8(0x52)
    S = c_uint8(0x53)
    T = c_uint8(0x54)
    U = c_uint8(0x55)
    V = c_uint8(0x56)
    W = c_uint8(0x57)
    X = c_uint8(0x58)
    Y = c_uint8(0x59)
    Z = c_uint8(0x5A)
    ENTER = c_uint8(0x0D)
    ESC = c_uint8(0x1B)
    SPACE = c_uint8(0x20)
    BACKSPACE = c_uint8(0x08)
    TAB = c_uint8(0x09)
    SHIFT = c_uint8(0x10)
    ONE = c_uint8(0x31)
    TWO = c_uint8(0x32)
    THREE = c_uint8(0x33)
    FOUR = c_uint8(0x34)
    FIVE = c_uint8(0x35)
    SIX = c_uint8(0x36)
    SEVEN = c_uint8(0x37)
    EIGHT = c_uint8(0x38)
    NINE = c_uint8(0x39)
    ZERO = c_uint8(0x30)
    CONTROL = c_uint8(0x11)



class MYMouse:
    """
    NOTE: 鼠标操作类
    """
    Left_up = 0x04
    Left_down = 0x02
    Right_up = 0x08
    Right_down = 0x01
    Middle_up = 0x10
    Middle_down = 0x20
    Move = 0x0001
    MOUSEEVENTF_ABSOLUTE = 0x8000
    NotAnyOperation = 0x0000