from django.core.management import call_command
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_ow_combos.settings")


def migrate():
    print("##### Migrate #####")
    call_command("makemigrations")
    call_command("migrate")


if __name__ == "__main__":
    migrate()
