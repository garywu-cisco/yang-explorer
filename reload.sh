#!/bin/sh

if [ -f "v/bin/activate" ]; then
    echo "Activating virtualenv .."
    source v/bin/activate
fi

if [ ! -f "server/data/db.sqlite3" ]; then
    echo "Database does not exist!  Run setup.sh first!"
    exit false
fi

echo "Reloading modules from CXML..."
cd server
python manage.py reload_cxml
cd ..
