#!/usr/bin/env bash

set -o errexit  # Exit on error

pip install -r requirements.txt

echo "Collecting static files..."
python hello_api/manage.py collectstatic --noinput
ls -l hello_api/static/

echo "Migrating database..."
python hello_api/manage.py migrate
