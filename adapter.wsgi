import sys, os, bottle


sys.path= ['/srv/www/app/'] + sys.path
os.chdir(os.path.dirname(__file__))

from app import application



