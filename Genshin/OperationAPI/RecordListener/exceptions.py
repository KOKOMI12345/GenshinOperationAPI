'''自定义异常'''

class CustomException(Exception): ...

class DataFormatException(CustomException): ...
class OperationException(CustomException): ...
class KeyboardException(CustomException): ...
class MouseException(CustomException): ...
class VailudateException(CustomException): ...