@echo off
echo Starting AI Design System...
echo ------------------------------------------------
echo Please wait while the server starts...
echo ------------------------------------------------

:: This opens your Chrome/Edge browser automatically
start http://127.0.0.1:5000

:: This runs your Python code
python app1.py

:: This keeps the window open if there is an error
pause