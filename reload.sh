#!/bin/sh

if [[ $NOVENV != 1 ]]; then
    echo "Creating / Activating virtualenv .."
    if [ -f "v/bin/activate" ]; then
        source v/bin/activate
    else
        virtualenv v
        source v/bin/activate
    fi
fi

if [ ! -f "server/data/db.sqlite3" ]; then
    echo "Database does not exist!  Run setup.sh first!"
    exit false
fi

echo "Reloading modules from CXML..."
cd server
python manage.py reload_cxml
cd ..
