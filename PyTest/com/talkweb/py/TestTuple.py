# -*-coding:utf-8-*- 
'''
Created on 2013-5-15

@author: pimengjue
'''
import sys
def Main():
    '''
    tuple_name=("apple","banana","grape","orange") 
    print tuple_name[1] 
    print tuple_name[-1] 
    print tuple_name[-2] 
    print tuple_name[1:3] 
    
    print '-----------------' 
    tuple=(('t1','t2'),('t3','t4')) 
    print tuple[0][0] 
    print tuple[1][0] 
    
    
    tuple_name=("apple","banana","grape","orange") 
    a,b,c,d=tuple_name 
    print a,b,c,d 
    '''
    
    a=1 
    b=2 
    c=333
    a,b=b,a 
    #print a,b 
    
    print 'a' and 'b' 
    print 'c' and 'm' 
    
    
if __name__ == '__main__':
    Main()