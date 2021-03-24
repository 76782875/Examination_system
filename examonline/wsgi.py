"""
WSGI config for examonline project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.zjdlproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from zjdl.core.wsgi import get_wsgi_application

os.environ.setdefault('zjdl_SETTINGS_MODULE', 'examonline.settings')

application = get_wsgi_application()
