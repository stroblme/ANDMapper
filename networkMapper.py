import os
import subprocess

driveList = [r"\\192.168.1.114\share", r"\\10.200.200.4\share"]

for drive in driveList:

    if os.path.exists(drive):
        print(f"Selected drive {drive}")

        # Disconnect anything on S
        subprocess.call(r'net use s: /del', shell=True)

        # Connect to shared drive, use drive letter S
        subprocess.call(f'net use s: {drive}', shell=True)

        break

print("Done")