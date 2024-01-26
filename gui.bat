@echo off
IF NOT EXIST "venv" (
    echo "venv not found, creating..."
    python -m venv venv
    venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    install.bat
    python -m streamlit run instant_ngp/gui/app.py
) ELSE (
    echo "venv found, activating..."
    venv\Scripts\activate.bat
    python -m streamlit run instant_ngp/gui/app.py
)

pause >nul

