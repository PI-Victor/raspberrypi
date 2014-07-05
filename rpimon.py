import psutil

class MyDaemon(Daemon):
        def run(self):
                while True:
                        self.collect_stats()
                        time.sleep(5)

        def collect_stats(self):
                cpu_time = psutil.cpu_times_percent(interval=1, percpu=False)
                file_handler = open('/home/vectra/projects/debug.log','a')
                file_handler.write(str(cpu_time))
                file_handler.close()


if __name__ == "__main__":
        daemon = MyDaemon('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
