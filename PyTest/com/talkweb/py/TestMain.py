#-*-coding:utf-8-*- 
'''
Created on 2013-5-15

@author: pimengjue
'''


import sys

def Main():
    '''
    sys.stdout.write("��ʼ\n")
    i=1
    print i,type(i),id(i)
    i=1000000000000
    print i,type(i),id(i)
    i=1.1
    print i,type(i),id(i)
    
    
    str1='i am "python"\n' 
    str2="i am 'Python' \r" 
    str3=""" 
               i'm "Python", 
               <a href="http://www.sina.com.cn"></a> 
              """ 

    #����԰�html ֮��Ķ�����ֱ��Ū����������Ҫ���� 
    print str1,str2,str3 
    
    
    array=[1,2,3] 
    print array[0] #1

    array[0]='a' 
    print array #['a',2,3]

    L=[123,'spam',1.23] 

    #�����С 
    print len(L) #3
    print L[0] #123

    print L[:-1]#���������һ�� [123, 'spam']
    print L+[4,5,6]#����ƴ��һ���µ��б�  [123, 'spam', 1.23, 4, 5, 6]
    '''
    '''
    test=['never',1,2,'yes',1,'no','maybe']
    test2=[[1,2,3],[4,5,6]]
    test3=[1,1,2,3,4,2]
    #test.sort()
    #test.reverse()
    #print test[0:3]#����test[0],������test[3] 
    #print test[0:6:2]#����test[0],������test[6],���Ҳ���Ϊ2 
    #print test[0:len(test)]#������ʼ,���������һ�� 
    #print test[-3:]#��ȡ���3 ��
    #for s in test:
    #   print s
    
    col1=[row[1] for row in test2]#��������ȡ�ڶ���
    print col1
    col3=[row[1]+1 for row in test2]
    print col3
    col4=[row[1] for row in test2 if row[1]%2==0]
    print col4
    print list(set(test3))
    '''
    
if __name__ == '__main__':
    Main()