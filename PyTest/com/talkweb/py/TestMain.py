#-*-coding:utf-8-*- 
'''
Created on 2013-5-15

@author: pimengjue
'''


import sys

def Main():
    '''
    sys.stdout.write("开始\n")
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

    #你可以把html 之类的东西都直接弄进来而不需要处理 
    print str1,str2,str3 
    
    
    array=[1,2,3] 
    print array[0] #1

    array[0]='a' 
    print array #['a',2,3]

    L=[123,'spam',1.23] 

    #输出大小 
    print len(L) #3
    print L[0] #123

    print L[:-1]#不包含最后一个 [123, 'spam']
    print L+[4,5,6]#重新拼接一个新的列表  [123, 'spam', 1.23, 4, 5, 6]
    '''
    '''
    test=['never',1,2,'yes',1,'no','maybe']
    test2=[[1,2,3],[4,5,6]]
    test3=[1,1,2,3,4,2]
    #test.sort()
    #test.reverse()
    #print test[0:3]#包括test[0],不包括test[3] 
    #print test[0:6:2]#包括test[0],不包括test[6],而且步长为2 
    #print test[0:len(test)]#包括开始,不包括最后一个 
    #print test[-3:]#抽取最后3 个
    #for s in test:
    #   print s
    
    col1=[row[1] for row in test2]#矩阵中提取第二列
    print col1
    col3=[row[1]+1 for row in test2]
    print col3
    col4=[row[1] for row in test2 if row[1]%2==0]
    print col4
    print list(set(test3))
    '''
    
if __name__ == '__main__':
    Main()