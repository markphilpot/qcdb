import os
import sys
sys.path.append('/home/mphilpot/htdocs')

os.environ['DJANGO_SETTINGS_MODULE'] = 'qcdb.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
