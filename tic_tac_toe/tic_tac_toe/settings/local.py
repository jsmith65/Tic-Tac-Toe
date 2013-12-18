from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

DATABASES = {
	"default": {
	"ENGINE": "django.db.backends.mysql",
	"NAME": "tictactoe",
	"USER": "jsmith65",
	"PASSWORD": "password",
	"HOST": "localhost",
	"PORT": "",
	}
}

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)

MIDDLEWARE_CLASSES += \
("debug_toolbar.middleware.DebugToolbarMiddleware", )

TIME_ZONE = 'America/Chicago'