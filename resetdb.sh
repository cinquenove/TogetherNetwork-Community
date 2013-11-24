#!/bin/bash
# -*- coding=utf-8 -*-

if [[ $@ == **sure** ]]; then
    echo -n "- Reset database: "
        heroku pg:reset DATABASE_URL --confirm together-network &> /dev/null
    echo "done"
    exit 0
fi

echo -n "- Reset database: "
echo "failed"
echo ""
echo "use 'cleandb.sh sure' if you are sure of what you are doing!"
