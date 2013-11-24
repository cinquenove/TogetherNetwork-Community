#!/bin/bash
# -*- coding=utf-8 -*-

if [[ $@ == **sure** ]]; then
    echo -n "- Cleaning the database: "
        python manage.py reset_db --noinput
    echo "done"
    exit 0
fi

echo -n "- Cleaning the database: "
echo "failed"
echo ""
echo "use 'cleandb.sh sure' if you are sure of what you are doing!"
