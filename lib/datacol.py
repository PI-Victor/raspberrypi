import threading, os, platform, time, psutil as ps
from time import gmtime, strftime
from lib.sqlhandler import DbQuery as db


class Scheduler(threading.Thread):
    '''
        Starts a collector that inserts data into the sqlite3 db 
        every 30 second.
        saves a log
    '''
    snooze = 5
    gettag = "Scheduler started every %s" % snooze + " seconds"

    def __init__(self):

        threading.Thread.__init__(self)
        ProcessLog(self.gettag)
        self.daemon = True

    def run(self):
        while True:
            temp = self.get_sysusage() 
            ProcessLog(temp)
            ProcessLog(str(db().ins_rec('usage',temp)))
            time.sleep(self.snooze-1)

    def get_sysusage(self):
        ''' 1st CPU Usage - 1 s delay for better cpu usage pull
            2nd % of used memory
            3rd % of swap used
        '''
        return ', '.join([str(ps.cpu_percent(1)), str(ps.virtual_memory()[2]) , str(ps.swap_memory()[3])])


class Collector(object):
    '''
        These are the function to be executed by the scheduler
        system collection and later on insertion to SQL
    '''
    gettag = "---=Server Start=---"
    def start_collector(self):
        ProcessLog(self.gettag)
        thread = Scheduler()
        thread.start()

class ProcessLog(object):
    '''
        keeps a log with processes and such
    '''
    def __init__(self,datastr):
        self.fileh = self.start_log()
        self.wrlog(datastr)
        self.fileh.close()

    def start_log(self):
        logpath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'l\
ogs'))
        filepath = os.path.join(logpath, 'collector.log')
        try:
            fileh = open(filepath, 'a')
            return fileh
        except IOError as e:
            print "Can't open collector log, check logs/ dir"

    def wrlog(self, datastr):
        self.fileh.write(' '.join([self.get_time(), datastr, '\n']))

    def get_time(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())
