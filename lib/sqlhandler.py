import sqlite3
from lib.datacol import ProcessLog

class DbQuery(object):
    '''
         Sqlite handler class, returns row fetched, or just writes to
         db tables values that are inserted
    '''
    def __init__(self):
        self.db = 'db/raspdb.db'
        self.con = sqlite3.connect(self.db)
        self.c = self.con.cursor()
        self.logger = ProcessLog()

    def get_rec(self,table):
        self.gettag = "From get_rec in DbQuery : "
        selrec = "SELECT * FROM " + table
        self.logger.wrlog(' '.join([self.gettag,selrec]))
        c = self.c.execute(selrec)
        result = c.fetchall()
        c.close()
        return result


