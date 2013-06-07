# -*-coding:utf-8-*- 
'''
Created on 2013-5-15

@author: pimengjue
'''
import sys
def Main(): 
    class A: 
        def __init__(self): 
            self.x=1 
    a=A() 
    print a.x
    
    class Student: 
        def __init__(self,name,age): 
            self.__name=name 
            self.__age=age 
        def getName(self): 
            format="my name is %s my age is %d"%(self.__name,self.__age) 
            print format 
        def __del__(self): 
            print self.__name
            print self.__age
            print "del" 
    if __name__=="__main__": 
        student=Student("chu",35) 
        student.getName() 
     
    
if __name__ == '__main__':
    Main()