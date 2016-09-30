"""
Django settings for mydjango project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gtk@uz%^ulsttma&)v1g509z8v3v9uem$(xl9!zuw88hi5gc^4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID =1

# Application definition

INSTALLED_APPS = [

    #apps
    'blog',
    'taggit',
    'rest_framework',
    'account',
    'images',

    #installed by default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #sitemap
    'django.contrib.sites',
    'django.contrib.sitemaps',

    #dev
    'debug_toolbar',
    'django_extensions',
    'django.contrib.admindocs',
    #'django.contrib.databrowse',

    #social network
    'social.apps.django_app.default',

    'sorl.thumbnail',
]

INTERNAL_IPS = ('127.0.0.1',)  # Used by app debug_toolbar


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mydjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '..//', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG, #rajout pour activer le débogage de django et de ses templates pour django>=1.8
        },
    },
]

WSGI_APPLICATION = 'mydjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../../../../../db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

#modifié
LANGUAGE_CODE = 'fr-fr'

#modifié
TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..//', 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'mydjango/../static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')

#en options ???
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
TEMPLATES_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'lhostevincent@gmail.com'
EMAIL_HOST_PASSWORD = 'popi2013'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
}


from django.core.urlresolvers import reverse_lazy

LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')


# to be able to authenticate with email and also Social Net
AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social.backends.facebook.Facebook2OAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOAuth2',
)


# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '300610793643444' # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'af36a2e24a7cd34108e474d6d82ae732' # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']


#Twitter
SOCIAL_AUTH_TWITTER_KEY = 'htNsFy5c4g1i3uF8Xnam9UwMW' # Twitter Consumer Key
SOCIAL_AUTH_TWITTER_SECRET = 'C720lqzdmSUp9eKjvezcTAwIj2aaCUzwDunH8zMPYGQSHTe4jC' # Twitter Consumer Secret


#Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '436363011747-icln3m1bnu96kha1n0v16l3oihua4rsg.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'MafQ_r30wG6m7dga6TmgSFUs' # Google Consumer Secret


#Thumbnail
THUMBNAIL_DEBUG = True