#!/usr/bin/env python
# Basic Example of multiprocessing threading with a limit of how many threads to use
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

report =[]

def test(nothingtoseehere):
        report.append("Test - " + str(nothingtoseehere))
        print("Test - " + str(nothingtoseehere))
        time.sleep(.5)


threadcount = 5 #Max amount of threads
data = range(20) #Data or list of items to run function against
pool = ThreadPool(threadcount)
print "\n\n ########### Below is the live theaded data ########### \n\n"

pool.map(test,data)
pool.close()
pool.join()

print "\n\n ########### Below is the appened data ########### \n\n"
for i in report:
    print i
