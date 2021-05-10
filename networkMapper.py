import os
import subprocess

root = "./"

driveA = r"\\192.168.1.114\share" #preferred
driveB = r"\\10.200.200.4\share"

if os.path.exists(driveA):
    drive = driveA
elif os.path.exists(driveB):
    drive = driveB
else:
    print("None of the drives available")
    exit

print(f"Selected drive {drive}")

# Disconnect anything on S
subprocess.call(r'net use s: /del', shell=True)

# Connect to shared drive, use drive letter S
subprocess.call(f'net use s: {drive}', shell=True)