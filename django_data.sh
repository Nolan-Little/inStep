# !/bin/bash

# Author - Zac Jones
# This bash script cleans out migrations, reruns them
# currently does NOT run seeder file, but if that is added later, uncomment line 13 and it will run that file

find ./$1/migrations/ -type f -name "*.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find ./$1/migrations/ -type f -name "*.pyc" -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py migrate; #runs the migration.
python manage.py makemigrations $1; #creates the migration.
python manage.py migrate; #runs the migration.
python manage.py loaddata volunteer.json #runs the file we created above to seed the new db