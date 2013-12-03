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

echo -n "- Cleaning the environment: "
    python ./manage.py clearsessions &> /dev/null
echo "done"

if [[ $@ == **sync** ]]; then
#    echo -n "- Synchronizing static files: "
#        python ./manage.py collectstatic --noinput &> /dev/null
#    echo "done"

    echo -n "- Synchronizing database: "
        python ./manage.py syncdb &> /dev/null
    echo "done"
fi

echo "Starting the server: "
    open http://127.0.0.1:5000/ &
    honcho start
    #foreman start

echo -n "Press enter to continue... " ; read