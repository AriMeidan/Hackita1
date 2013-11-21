'''
Created on Nov 20, 2013

@author: ari
'''


def bottleCount(num):
    if num < 0:
        return
    print "there are %d" % num, "on the wall"
    bottleCount(num - 1)


def HelloWorld(s):
    return "Hello %s" % s


bottleCount(30)
