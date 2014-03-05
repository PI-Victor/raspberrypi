import threading, os, platform, time, threading
from time import gmtime, strftime

class Scheduler(threading.Thread):
    '''
        Starts a collector that inserts data into the sqlite3 db 
        every 30 second.
        saves a log
    '''
    def __init__(self):
        threading.Thread.__init__(self)
        self.snooze = 10
        self.gettag = "Scheduler started every %s" % self.snooze + " seconds"
        ProcessLog(self.gettag)
        
    def run(self):
        ProcessLog("Thread Run")
        while True:
            ProcessLog(self.get_sysinfo())
            time.sleep(self.snooze)

    def get_sysinfo(self):
        return str(platform.uname())


class Collector(object):
    '''
        These are the function to be executed by the scheduler
        system collection and later on insertion to SQL
    '''
    def __init__(self):
        ProcessLog("===Server Started===")

    def start_collector(self):
        sch = Scheduler()
        sch.daemon = True
        sch.start()

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
#        print "got here"

    def get_time(self):
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())
    

        
        
