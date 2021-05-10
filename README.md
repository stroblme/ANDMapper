# ANDMapper - Automatic Network Drive Mapper

Checks a list of network locations, sorted by preference, for availability and maps the first successful lookup to a predefined Windows network drive.

## Setup

1. Update the list inside ```src/andMapper.py``` depending on your network location and the drive letter you want.

2. I recommend to test the script now, before proceeding with the next step.

3. Install requirements (only pyinstaller) and run the build skript to generate an executable.

   - >```pip install -r requirements/base.txt```
   - >```cd src```
   - >```./build.cmd```

4. Afterwards, this executable (inside ```src/dist/andMapper/andMapper.exe```) can then be linked from the startup folder to enable this at autostart.
