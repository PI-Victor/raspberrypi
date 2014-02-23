import sys, os, bottle

sys.path = ['/srv/www/app/src'] + sys.path
os.chdir(os.path.dirname(__file__))

import app # This loads your application

application = bottle.default_app()