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
    print a #a �е�Ԫ�ؾ���b ������
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
       ����Ҫ�����ڡ�=�����������½�һ���µı������渳ֵ�����Ȼ���ٰ�������ָ��=����ߣ����޸���ԭ�� 
      ��p ���ã�ʹp ��Ϊָ���¸�ֵ���������á���+=���ᣬֱ���޸���ԭ��p ���õ����ݣ���ʵ��+=��=��python 
      �ڲ�ʹ���˲�ͬ��ʵ�ֺ����� 
'''