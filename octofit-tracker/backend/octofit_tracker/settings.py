# settings.py for Django project

INSTALLED_APPS = [
    # ...existing apps...
    'djongo',
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your-database-name',
    }
}

# Add other necessary settings below as needed.
