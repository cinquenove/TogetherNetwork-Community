#!/bin/bash

source venv/bin/activate
cd togethernetwork
pip install -U -r requirements.txt

screen -S togethernetwork -X quit &> /dev/null
echo "Sleeping 1 second..."
sleep 1
screen -S togethernetwork ./runserver.sh