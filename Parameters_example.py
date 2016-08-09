#!/usr/bin/env python
#Basic example of passing parameters from function to function 

def function_A():
    data = 5
    data1 = 15
    if host == 1:
        work(data, data1)
    else:
        function_B()

def function_B():
    data = 3
    data1 = 13
    work(data, data1)

def work(data,data1):
    print data
    print data1

if __name__ == '__main__':
    host = 11
    function_A()
