#!/bin/bash

set -a;
source .env;
set +a;
if [ -n "$1" ]; then
    python django/manage.py $1 $2 $3
else 
    python django/manage.py runserver
fi
exit 0
