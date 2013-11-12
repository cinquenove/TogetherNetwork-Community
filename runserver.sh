#!/bin/bash
# -*- coding=utf-8 -*-

echo -n "- Creating a virtual environment: "
    virtualenv venv -v &> /dev/null
    source venv/bin/activate
echo "done"

echo -n "- Upgrading dependencies inside the virtual environment: "
    pip install -q -U -r togethernetwork/requirements.txt
echo "done"

echo -n "- Synchronizing dependencies inside the virtual environment: "
    python ./manage.py clearsessions
    python ./manage.py syncdb
echo "done"

echo "Starting the server: "
    honcho start
    #foreman start

echo -n "Press enter to continue... " ; read