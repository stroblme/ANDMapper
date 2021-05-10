# ANDMapper - Automatic Network Drive Mapper

Checks a list of network locations, sorted by preference, for availability and maps the first successful lookup to a predefined Windows network drive.

## Setup

Install requirements (only pyinstaller) and run the build skript to generate an executable.

1. ```pip install -r requirements/base.txt```
2. ```cd src```
3. ```./build.cmd```

Afterwards, this executable (inside ```src/dist/andMapper/andMapper.exe```) can then be linked from the startup folder to enable this at autostart.
