#!/usr/bin/python3.9
import shutil
import psutil
from network import *

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > 80

if check_cpu_usage() and check_localhost():
    print("ok")
else:
    print("not ok")
