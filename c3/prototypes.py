import os
import sys

from django.conf import settings


BASE_DIR = os.path.dirname(__file__)


settings.configure(
	DEBUG=True,
	SECRET_KEY='thisissecretkey',
	ROOT_URLCONF='sitebuilder.urls',
	MIDDLEWARE_CLASSES=(),
	INSTALLED_APPS=(
		'django.contrib.staticfiles',
		#'django.contrib.webdesign',
		'sitebuilder',
	),
	TEMPLATES = (
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [
	            os.path.join(BASE_DIR, 'templates'),
	        ],
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [],
	        },
	    },
	),
	STATICFILES_DIRS=(
		os.path.join(BASE_DIR, 'static'),
	),
	STATIC_URL='/static/',
	SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
)


if __name__ == "__main__":
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
