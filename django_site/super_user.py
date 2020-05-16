import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django
django.setup()

from django.contrib.auth.models import User


def create_super_user(username="admin", password="adminadmin"):
    try:
        u = User(username=username)
        u.set_password(password)
        u.is_superuser = True
        u.is_staff = True
        u.save()
        print("Username \"" + username + "\" created!")
    except Exception as e:
        print("Error while trying to create admin superuser\nError:\t" + str(e))


if __name__ == "__main__":
    create_super_user()
