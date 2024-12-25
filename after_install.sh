#!/bin/bash
# Navigate to the Django app directory
cd /home/ec2-user/mengutech
# Activate the virtual environment (if applicable)
source /home/ec2-user/mengutech/venv/bin/activate
# Install required Python packages
pip install -r requirements.txt
# Run Django migrations
python manage.py migrate --noinput
# Collect static files
python manage.py collectstatic --noinput
# Deactivate the virtual environment
deactivate
