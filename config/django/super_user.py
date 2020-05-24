import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_ow_combos.settings")
import django
django.setup()
from django.contrib.auth.models import User
from _ow_combos.sys.client_arguments import get_cli_args
variables = get_cli_args()

if not all(["username", "password"] in list(variables.keys())):
    raise Exception("Requirement parameters \"username\" and \"password\" not informed")
if variables("username") is None or variables("password") is None:
    raise Exception("Requirement parameters \"username\" and \"password\" can't be null")


def create_super_user():
    try:
        u = User(username=variables("username"))
        u.set_password(variables("password"))
        u.is_superuser = True
        u.is_staff = True
        u.save()
        print("Username \"" + variables("username") + "\" created!")
    except Exception as e:
        print("Error while trying to create admin superuser\nError:\t" + str(e))


if __name__ == "__main__":
    create_super_user()
