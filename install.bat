@echo off

REM Check if virtual environment is activated
if defined VIRTUAL_ENV (
    echo Virtual environment is already activated.
) else (
    echo Virtual environment is not activated. Activating now...
    CALL venv\Scripts\activate.bat
)

python scripts/install.py
