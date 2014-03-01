import bottle,sqlite3
from bottle import *



class DbQuery(object):
    '''
         Sqlite handler class, returns row fetched, or just writes to 
         db tables values that are inserted
    '''
    def __init__(self):
        self.db = 'db/raspdb.db'
        self.con = sqlite3.connect(self.db)
        self.c = self.con.cursor()

    def get_rec(self,table):
        selrec = "SELECT * FROM " + table
        print selrec
        c = self.c.execute(selrec)
        result = str(c.fetchall())
        c.close()
        return result


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
    mydb = DbQuery()
    results = mydb.get_rec('specs')
    return {'title': 'Specifications Raspberry Pi', 'results' : results ,'get_url' : url }

@route('/usage')
@view('usage')
def get_usage(title=''):
    return { 'title' : 'Usage statistics ', 'get_url' : url }

if __name__ == '__main__':
    #REMEMBER TO RUN DATA COLLECTION BEFORE STARTING THE SERVER
    #data_collect() and write to db, so server can take it from there when it starts
    run(host='192.168.15.103',port=5050,reloader=True, debug=True)
