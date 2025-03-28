#!/bin/bash

# Activate the virtual environment if needed
# source venv/bin/activate

# Run Locust with the specified host and options
locust -f locustfiles/main.py --host https://www.intelligarts.com --web-port 443