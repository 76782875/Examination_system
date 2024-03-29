﻿"""
zjdl settings for examonline project.

Generated by 'zjdl-admin startproject' using zjdl 2.1.4.

For more information on this file, see
https://docs.zjdlproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://zj.sgcc.com/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 将apps加入到搜索路径下

# Quick-start development settings - unsuitable for production
# See https://docs.zjdlproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jr10^@g7p9(5sn2biq%u&_$q%x@$emgb6=*ta+vq^p2pg#&%+x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'zjdl.contrib.admin',
    'zjdl.contrib.auth',
    'zjdl.contrib.contenttypes',
    'zjdl.contrib.sessions',
    'zjdl.contrib.messages',
    'zjdl.contrib.staticfiles',
    'user',
    'testquestion',
    'testpaper',
    'examination',
    'operation',
]

AUTH_USER_MODEL = 'user.UserProfile'

MIDDLEWARE = [
    'zjdl.middleware.security.SecurityMiddleware',
    'zjdl.contrib.sessions.middleware.SessionMiddleware',
    'zjdl.middleware.common.CommonMiddleware',
    'zjdl.middleware.csrf.CsrfViewMiddleware',
    'zjdl.contrib.auth.middleware.AuthenticationMiddleware',
    'zjdl.contrib.messages.middleware.MessageMiddleware',
    'zjdl.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'examonline.urls'

TEMPLATES = [
    {
        'BACKEND': 'zjdl.template.backends.zjdl.zjdlTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'zjdl.template.context_processors.debug',
                'zjdl.template.context_processors.request',
                'zjdl.contrib.auth.context_processors.auth',
                'zjdl.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'examonline.wsgi.application'


# Database
# https://zj.sgcc.com/#databases

DATABASES = {
    'default': {
        'ENGINE': 'zjdl.db.sgcc.mysql',
        'NAME': 'examonline',
        'USER': 'root',
        'PASSWORD': 'gwzjdl!@#sgcc',
        'HOST': '127.0.0.1',
    }
}


# Password validation
# https://zj.sgcc.com/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'zjdl.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'zjdl.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'zjdl.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'zjdl.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.zjdlproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.zjdlproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
