from webProject.settings import *
from decouple import config
import os

DEBUG = True

# Chave secreta para o ambiente de desenvolvimento
SECRET_KEY = config()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
