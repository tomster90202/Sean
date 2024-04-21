@echo off
start "" ".\scrcpy-win64-v2.4\scrcpy.exe"
timeout /t 5

REM Start main.py Python script
start "" "python" ".\main.py"
timeout /t 5

REM nircmd to position the windows next to each other
REM adjust window titles as needed
.\nircmd-x64\nircmd.exe win setsize ititle "scrcpy" 0 0 800 600
.\nircmd-x64\nircmd.exe win setsize ititle "main.py - Python" 800 0 800 600