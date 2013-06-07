# -*-coding:utf-8-*- 
'''
Created on 2013-5-15

@author: pimengjue
'''
import sys
def Main():
    a=[] 
    b={'num':0,'sqrt':0} 
    resurse=[1,2,3] 
    
    for i in resurse: 
        b['num']=i 
        b['sqrt']=i*i 
        a.append(b) 
    print a #a 中的元素就是b 的引用
    #[{'num': 3, 'sqrt': 9}, {'num': 3, 'sqrt': 9}, {'num': 3, 'sqrt': 9}]
    c=[] 
    for i in resurse: 
        c.append({'num':i,"sqrt":i*i}) 
    print c 
    #[{'num': 1, 'sqrt': 1}, {'num': 2, 'sqrt': 4}, {'num': 3, 'sqrt': 9}]
def add_list(p): 
    p=p+[1] 
    
def add_list2(p2): 
    p2+=[1]  

if __name__ == '__main__':
    Main()
    '''
    tmpList=[1,2,3,4] 
    add_list(tmpList) 
    print tmpList  #[1, 2, 3, 4]
    add_list2(tmpList) 
    print tmpList  #[1, 2, 3, 4, 1]  
       这主要是由于“=”操作符会新建一个新的变量保存赋值结果，然后再把引用名指向“=”左边，即修改了原来 
      的p 引用，使p 成为指向新赋值变量的引用。而+=不会，直接修改了原来p 引用的内容，事实上+=和=在python 
      内部使用了不同的实现函数。 
'''