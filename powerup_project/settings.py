# powerup_project/settings.py
INSTALLED_APPS = [
    ...
    'powerup_app',
    'django.contrib.staticfiles',
]
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
