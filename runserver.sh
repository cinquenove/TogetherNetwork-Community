#!/bin/bash

echo -n "Killing old process: "
screen -S togethernetwork -X quit &> /dev/null
echo "done"

echo -n "Upgrading dependencies inside the virtual environment: "
source venv/bin/activate
cd togethernetwork
pip install -U -r requirements.txt
echo "done"

echo "Sleeping 1 second before creating a new screen..."
sleep 1
screen -S togethernetwork ./runserver.sh