# settings.py

# Standard Django settings...

# MongoDB Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

# CORS Configuration
INSTALLED_APPS = [
    # ...existing apps...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'
]
CORS_ALLOW_HEADERS = [
    '*'
]

ALLOWED_HOSTS = ['*']
