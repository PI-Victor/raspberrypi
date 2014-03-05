import sqlite3
#from lib.datacol import ProcessLog

class DbQuery(object):
    '''
         Sqlite handler class, returns row fetched, or just writes to
         db tables values that are inserted
    '''
    gettag = "Created SQL Handler"
    def __init__(self):
        self.db = 'db/raspdb.db'
        self.con = sqlite3.connect(self.db)
        self.c = self.con.cursor()

    def get_rec(self,table):
        self.gettag = "SELECT * FROM " + table
        c = self.c.execute(self.gettag)
        result = c.fetchall()
        c.close()
        return result

    def ins_rec(self, table, datastr):
        self.gettag = ' '.join(["INSERT INTO",table ,"VALUES(",datastr,")"])
#        return self.gettag
        c = self.c.execute(self.gettag)
        self.con.commit()        
        c.close()
        return 
