import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_sitio.settings')
django.setup()

from django.contrib.auth.models import User

# Cambia 'admin' y 'tu_password_segura' por lo que quieras
username = 'admin'
password = 'Carrillo.2004'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, password)
    print(f"Superusuario '{username}' creado con éxito.")
else:
    print(f"El usuario '{username}' ya existe.")