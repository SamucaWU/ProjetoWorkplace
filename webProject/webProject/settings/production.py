from webProject.settings import *
from decouple import config
import os

DEBUG = False

# Chave secreta para o ambiente de desenvolvimento
SECRET_KEY = config('developer-admin-SENA!8*#&*&=5gv@vo3os8gep0a3elx3&2ps9w$14u-_dr(ow+ytzoideveloper-admin-SENA!-SamucsSlk')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}