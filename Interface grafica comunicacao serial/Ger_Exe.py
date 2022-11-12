import sys
from cx_Freeze import setup, Executable
from tkinter import *
from typing import List, Any
import serial.tools.list_ports
import serial
from tkinter import ttk, messagebox
from tkinter import filedialog
import CRC16_MODBUS
from time import sleep

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = [Executable("MPA23FILE.py", icon ="favicon.ico")]


setup(
    name="MPA23",
    version="0.1",
    description="Primeiro arquivo executável do software módulo de potência",
    options={"build_exe":{"packages":["serial","tkinter"],"include_files":["favicon.ico","RB.png"]}},
    executables= [Executable("MPA23FILE.py", base=base)]
)

