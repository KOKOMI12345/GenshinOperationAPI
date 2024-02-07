"""依赖的导入放这个文件夹"""
from datetime import datetime
from pynput import keyboard , mouse
from RecordListener.RecordLog import LogManager #自定义
from RecordListener.DataProcess import translate #自定义
from RecordListener.MouseKeyboardToSys import * #自定义
import json
import time
import os
from rich.progress import track
from RecordListener.exceptions import *
from RecordListener.vaildation import *
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread