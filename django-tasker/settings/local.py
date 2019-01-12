from .base import *

DEBUG = True

print('Base: {}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
