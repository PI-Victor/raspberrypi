import sys
from collection.daemon import Daemon
import psutil
import time
import logging
import os

#get current directory so i can create the debugging log in logs/
pid_path='/tmp/rpimon.pid'
workdir=os.path.dirname(os.path.realpath(__file__))
debug_log = '/'.join([workdir,'logs','debug.log'])

if not os.path.isdir(os.path.dirname(debug_log)):
        try:
                os.makedirs(os.path.dirname(debug_log))
        except OSError as e:
                exit("Can not create log path in current directory!!! - %s" %e )

def load_debugger():
        logging.basicConfig(filename = debug_log,
                            format = '%(asctime)s %(levelname)s:%(message)s',
                            filemode = 'a',
                            level = logging.DEBUG)

#just assign a temp path so that the log can be created
#daemon starts in / as work dir, can't create log there 
#with unpriviliged user, hard code for now

class MyDaemon(Daemon):
'''leave the daemon as it is, just override init to
specify output source for debugging
'''
        def __init__(self):
                self.stdin =
                self.stdout =
                self.stderr =
                self.pidfile = 
                
        def run(self):
                while True:
                        self.collect_stats()
                        time.sleep(5)

        def collect_stats(self):
                cpu_time = psutil.cpu_times_percent(interval=1, percpu=False)
                logging.info('Current CPU stats')
                flh.write(str(cpu_time))


if __name__ == "__main__":
        daemon = MyDaemon(pid_path)
        load_debugger()
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        logging.info('Started Daemon\n')
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        logging.critical('Stopped Daemon\n')
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        logging.info('Restarted Daemon\n')
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
