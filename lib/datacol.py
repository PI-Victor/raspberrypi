import threading, os, platform, time, multiprocessing 
from Queue import Queue

class Scheduler(multiprocessing.Process):
    '''
        Starts a collector that inserts data into the sqlite3 db 
        every 30 second.
        saves a log
    '''
    def __init__(self):
#        threading.Thread.__init__(self)
        self.logger = ProcessLog()
        self.snooze = 5
        self.gettag = "Scheduler started every %s" % self.snooze
        self.logger.wrlog(self.gettag)
 #       self.daemon = True
        
    def run(self):
       while True:
       #sleep and write to log before starting
           
        self.get_sysinfo()
        time.sleep(self.snooze)
        
    def get_sysinfo(self):
        self.cpu = platform.processor()
        self.logger.wrlog("Executed")
        print "was here"

    
class Collector(object):
    '''
        These are the function to be executed by the scheduler
        system collection and later on insertion to SQL
    '''
    def __init__(self):
        a = ''
    
    def wrtime(self):
        logger = ProcessLog()
        logger.wrlog(" --Server Start")


class ProcessLog(object):
    '''
        keeps a log with processes and such
    '''
    def __init__(self):
    #import time and get human readable time
        from time import gmtime, strftime
        self.time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        self.fileh = self.start_log() 

    def start_log(self):
        logpath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'l\
ogs'))
        filepath = os.path.join(logpath, 'collector.log')
        try:
            fileh = open(filepath, 'a')
            return fileh
        except IOError as e:
            print "Can't open collector log, check logs/ dir"
        
    def wrlog(self,datastr):
        self.fileh.write(' '.join([self.time, datastr, '\n']))
        
                 
        
        