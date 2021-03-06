#!/usr/bin/env python3
from network import *
import shutil
import psutil
def check_disk_usage(disk):
# verifies greater than 20 percent disk memory
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
# Verifies CPU usage is under 75
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Netowkr checks failed")