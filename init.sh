#!/bin/bash
echo -n "Cleaning & updating the local copy: "
git fetch --all >> /dev/null
git reset --hard origin/master  >> /dev/null
git pull >> /dev/null
echo "done"

echo -n "Creating a virtual environment: "
virtualenv venv -v >> /dev/null
echo "done"

echo -n "Installing dependencies inside the virtual environment: "
source venv/bin/activate
pip install -U -r togethernetwork/requirements.txt
echo "done"