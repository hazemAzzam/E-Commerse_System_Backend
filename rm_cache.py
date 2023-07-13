import os
import shutil

# store data into json file
#if os.path.exists("data.json"):
#    os.remove("data.json")
#os.system("python manage.py dumpdatautf8 --output data.json")

# get current project files and directories
cwd = os.listdir('.')

# get directories in the current project
directories = [name for name in cwd if os.path.isdir(name)]

for directory in directories:
    # get app/__pycache__/
    pycache = os.path.join(directory, "__pycache__")

    # get app/migrations/__pycache__/
    migrations = os.path.join(directory, "migrations")

    # get app/migrations/00*.py
    migrations_pycache = os.path.join(migrations, "__pycache__")
    try:
        migrations_files = [file for file in os.listdir(migrations) if file.startswith("00")]
    except:
        migrations_files = []

    # delete app/__pycache__/ 
    if os.path.exists(pycache):
        shutil.rmtree(pycache)

    # delete app/migrations/__pycache__/ 
    if os.path.exists(migrations_pycache):
        shutil.rmtree(migrations_pycache)
        print(f"{migrations_pycache} Deleted!")

    # delete 00*.py files
    for file in migrations_files:
        file_path = os.path.join(migrations, file)
        if os.path.exists(file_path):
            os.remove(file_path)

# get db.sqlite3
db_sqlite = os.path.join("db.sqlite3")

# delete db.sqlite3
if os.path.exists(db_sqlite):
    os.remove(db_sqlite)