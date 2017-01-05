from .base import *     # noqa

# Override static and media URL for prefix in WSGI server.
# https://code.djangoproject.com/ticket/25598
STATIC_URL = '/2016/static/'
MEDIA_URL = '/2016/media/'

CONFERENCE_DEFAULT_SLUG = 'pycontw-2016'
