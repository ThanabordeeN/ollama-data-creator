@echo off
REM Activate the new environment
call conda activate data_create
echo "Environment activated successfully"
echo "Intializing setup..."
REM Install requirements from requirements.txt
pip install -r requirements.txt --quiet
echo "Requirements installed successfully"
REM Run the main.py script
python main/main.py

pause