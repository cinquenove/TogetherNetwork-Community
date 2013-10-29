#!/bin/bash
# -*- coding=utf-8 -*-

#python ./manage.py makemessages -l en
#python ./manage.py makemessages -l it
#python ./manage.py compilemessages

# python ./manage.py schemamigration Teas --auto
# python ./manage.py schemamigration Profiles --auto
# python ./manage.py schemamigration Groups --auto

python ./manage.py syncdb
#python ./manage.py migrate
python ./manage.py clearsessions

if [[ $EUID -ne 0 ]]; then
    #honcho -f Procfile start --port 8000
    python ./manage.py runserver 0.0.0.0:8000
else
    #honcho -f Procfile start --port 80
    python ./manage.py runserver 0.0.0.0:80
fi

echo -n "Press enter to continue... " ; read