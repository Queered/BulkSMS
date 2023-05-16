#!/bin/bash

# get required packages
apt-get update
apt-get install -y termux-api python

# make a virtual environment
python -m venv sms-env
source sms-env/bin/activate

# install required Python packages
pip install click

# wget the script from GitHub
wget https://raw.githubusercontent.com/Queered/BulkSMS/main/main.py

# make the script executable
chmod +x send_sms.py

echo "Installation completed successfully."
echo "To send bulk SMS messages, run the following command:"
echo "python send_sms.py"
