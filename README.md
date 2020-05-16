# Overwatch Combos
Experiment with possible combinations of team roasters, including hero abilities.

###Setting up the environment
* [Install Python 3.8](https://www.python.org/downloads/)
* Clone the project
* Create a virtual environment **(optional)**
* In the project's root run ```pip3 install -r ./requirements.txt```

###Django
Create django-admin superuser by editing and running ```python3 django_site/super_user.py```

###Deploy
```
python3 django_site/manage.py makemigrations
python3 django_site/manage.py migrate
python3 django_site/manage.py runserver 8000
```
