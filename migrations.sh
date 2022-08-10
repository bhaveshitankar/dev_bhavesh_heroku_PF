args=("$@")


python3 manage.py makemigrations

python3 manage.py sqlmigrate ${args[0]} ${args[1]} 

python3 manage.py migrate
