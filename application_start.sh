# !/bin/bash
# Navigate to the Django app directory
cd /home/ec2-user/mamatjnalab_aws
# Activate the virtual environment
source /home/ec2-user/mamatjnalab_aws/venv/bin/activate
# Start the Gunicorn server (adjust settings as needed)
gunicorn --workers 3 --bind 0.0.0.0:8000 mamatjnalab_aws.wsgi:application --daemon
# Deactivate the virtual environment
deactivate
