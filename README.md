# Overwatch Combos
Experiment with possible combinations of team roasters, including hero abilities.


###Setting up the environment
* [Install Python3](https://www.python.org/downloads/)
* Clone the project
* Create a virtual environment **(optional but recommended)**
* In the project's root run ```pip3 install -r ./requirements.txt```


###Deploy
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000
```


###Django


######Super User
oCreate django-admin superuser by editing and running ```python ow_combos/super_user.py```

