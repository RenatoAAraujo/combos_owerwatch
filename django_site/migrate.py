from django.core.management import call_command

print("##### Migrate #####")
call_command("migrate")
call_command("makemigrations")

print("##### Create Tables #####")
# call_command("sqlmigrate", "")

print("##### Load Initial Data #####")
call_command("loaddata", "initial_data.json")

print("##### Synchroninsing Database #####")
call_command("syncdb")
call_command("loaddata", "initial_data.json")
