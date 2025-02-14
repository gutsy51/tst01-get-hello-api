#!/usr/bin/env bash

set -o errexit  # Exit on error

pip install -r requirements.txt

python hello_api/manage.py collectstatic --noinput
