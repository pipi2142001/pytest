# -*-coding:utf-8-*- 
'''
Created on 2013-5-15

@author: pimengjue
'''
import sys
def Main():
    a=[133,224,2344,2243,22342,224,133,133,989] 
    b=set(a) 
    print b 
    
    a=[133,224,2344,2243,22342,224,133,133,989] 
    b=set(a) 
    print b 
    a=["11","22","33","33"] 
    b=["11","33"] 
    c=set(a)&set(b) 
    print c 
    
if __name__ == '__main__':
    Main()