#!/bin/bash

source venv/bin/activate
pip install -U -r requirements.txt
cd togethernetwork

screen -S togethernetwork -X quit &> /dev/null
echo "Sleeping 1 second..."
sleep 1
screen -S togethernetwork ./runserver.sh