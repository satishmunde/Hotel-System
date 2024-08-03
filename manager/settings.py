"""
Django settings for manager project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=w3^*2o3vme!qefs81%1osr%q39yv13i1o3!^*t2z8y8k)-u=m"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
     'django_filters',
    'core',
    "api",
    "billing",
    "id_generator",
    "token_system",
    'corsheaders',
    'inventory',
    "menu",
    "orders",
    "employees",
    'drf_yasg',
     'debug_toolbar',
    "crm",
    'rest_framework', 
    'channels',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.cache.CacheMiddleware',
]

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 15
CACHE_MIDDLEWARE_KEY_PREFIX = ''

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # Other backends if needed
]


LOGOUT_REDIRECT_URL = '/login/'  

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}

ROOT_URLCONF = "manager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR,"templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "manager.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'hotel_system',
#         'USER': 'postgres',
#         'PASSWORD': 'Admin',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6380/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'default'


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

ASGI_APPLICATION = 'manager.asgi.application'

SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = True




SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # Use cache-based sessions
SESSION_CACHE_ALIAS = 'default'  # Points to the cache backend configured above


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


STATICFILES_DIRS = [BASE_DIR,'static']

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = "/media/"

REST_FRAMEWORK = {
    'CORE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    
}




SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),

    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
} 

DJOSER = {
    'SERIALIZERS':{ 
        'user_create':'core.serializers.UserCreateSerializer',
        'current_user':'core.serializers.LoginSystemSerializer',
        'user': 'core.serializers.LoginSystemSerializer', 
        
    }

}



AUTH_USER_MODEL ='core.LoginSystem'



CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1",
    "http://127.0.0.1:64120",
]



SWAGGER_SETTINGS = {
    
    'VALIDATOR_URL': 'http://127.0.0.1:8000',
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },

}

REDOC_SETTINGS = {
   'LAZY_RENDERING': False,

}


LOGIN_URL = '/login/?next=/'  # Adjust this URL according to your login page URL




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail's SMTP server
EMAIL_PORT = 587  # Port for TLS
EMAIL_USE_TLS = True  # Use TLS
EMAIL_USE_SSL = False  # Do not use SSL (use TLS instead)
EMAIL_HOST_USER = 'satishmh26@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'gdug zoaf enta zjia'  #    gdug zoaf enta zjia
DEFAULT_FROM_EMAIL = 'satishmh26@gmail.com'  # Default "From" email address
