#!/usr/bin/env python
# Basic Example of semaphore threading with a limit of how many threads to use
import threading, time
from threading import Thread, Semaphore

threads = []
report = []

class test(Thread):
        def __init__(self):
                Thread.__init__(self)

        def run(self):
                pool.acquire()
                time.sleep(.5)
                print "HI"
                report.append("HI")
                time.sleep(.5)
                print "AFTER 2nd sleep"
                report.append("AFTER 2nd sleep")
                pool.release()
                return

threadcount = 5 #Max number of threads to open
data = range(10)
pool = Semaphore(threadcount)
print "\n\n ########### Below is the live theaded data ########### \n\n"

for host in data:
                thread = test()
                threads.append(thread)
                thread.start()
for t in threads:
        t.join()

print "\n\n ########### Below is the appened data ########### \n\n"
for i in report:
    print i
