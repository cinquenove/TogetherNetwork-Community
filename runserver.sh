#!/bin/bash
# -*- coding=utf-8 -*-

echo -n "- Creating a virtual environment: "
    virtualenv venv -v &> /dev/null
    source venv/bin/activate
echo "done"

if [[ $@ == **upgrade** ]]; then
    echo -n "- Upgrading dependencies inside the virtual environment: "
        pip install -q -U -r requirements.txt
    echo "done"
fi

echo -n "- Synchronizing database: "
    python ./manage.py clearsessions &> /dev/null
    python ./manage.py syncdb &> /dev/null
echo "done"

echo "Starting the server: "
    honcho start
    #foreman start

echo -n "Press enter to continue... " ; read