from django.contrib.auth.models import User

try:
    User.objects.create_superuser(username='admin', password='123', email='')
except Exception as e:
    print("Error while trying to create admin superuser\nError:\t" + str(e))
