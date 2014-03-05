import threading
from time import gmtime, strftime, sleep


class doThread(threading.Thread):
    _snooze = 10
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
#        self.get_time()

    def get_time(self):
        while True:
            hourly = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            print "The time is refreshed every %s seconds " % self._snooze ,  hourly
            sleep(self._snooze)

if __name__ == "__main__":
    tr = doThread()
    tr.daemon = True
    tr.start()
#    push = doThread()
#    push.daemon = True
#    push.start()
    print "It also has to get here"
