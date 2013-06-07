# -*-coding:utf-8-*- 
'''
Created on 2013-5-15

@author: pimengjue
'''
import sys
import io

def Main():
    
    try: 
        file=open('firstpython.py')
        s=file.readline()
        print s
    except IOError,(errno,strerror): 
        print "I/O error(%s):%s" %(errno,strerror) 
    except ValueError: 
        print "Could not convert data to an integer" 
    except: 
        print "Unexpected error:",sys.exc_info()[0] 
        raise 
    finally: 
        file.close() 
    
if __name__ == '__main__':
    Main()