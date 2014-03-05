from bottle import *
from lib.sqlhandler import *
from lib.datacol import * 
import sqlite3

@route('/static/:filename#.*#', name='static')
def server_static(filename):
    return static_file(filename, root='static')

@route('/')
@view('home')
def index(title=''):
    return { 'title': 'Raspberry Pi Monitor', 'get_url': url  }

@route('/specs')
@view('specs')
def get_specs(title=''):
    results = DbQuery().get_rec('specs')
    return {'title': 'Specifications Raspberry Pi', 'results' : results ,'get_url' : url }

@route('/usage')
@view('usage')
def get_usage(title=''):
    return { 'title' : 'Usage statistics ', 'get_url' : url }

if __name__ == '__main__':
    #REMEMBER TO RUN DATA COLLECTION BEFORE STARTING THE SERVER
    #data_collect() and write to db, so server can take it from there when it starts
    collect = Collector().start_collector()
#    collect.start_collector()
    run(host='192.168.15.103',port=5050,reloader=True, debug=True)
