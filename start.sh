#!/bin/bash
path=$(dirname "$0")
# set -a: Mark variables and function which are modified or created for export to the environment of subsequent commands
set -a;
source $path/.env;
set +a;
if [ -n "$1" ]; then
    python $path/django/manage.py $1 $2 $3
else 
    python $path/django/manage.py runserver
fi
exit 0
