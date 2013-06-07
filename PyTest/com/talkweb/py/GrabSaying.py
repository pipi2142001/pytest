# -*-coding:utf-8-*- 
'''
Created on 2013-5-15
http://pythonhosted.org/APScheduler/cronschedule.html
@author: pimengjue 
'''
import datetime
import urllib
import MySQLdb
from apscheduler.scheduler import Scheduler
import logging 

    
logging.basicConfig()

schedudler = Scheduler(daemonic = False)

def do_delete(cursor,db,say):
    sql = "delete from verycd_saying where saying='%s'"%(say)
    try:
        cursor.execute(sql)
        db.commit()
        print "delete success"
    except MySQLdb.Error,e:
        print "Error: %s" % e
        db.rollback()  
        
def do_insert(cursor,db,say,createtime):
    sql = "insert into verycd_saying(saying,createtime) values('%s','%s')"%(say,createtime)
    try:
        cursor.execute(sql)
        db.commit()
        print "insert success"
    except MySQLdb.Error,e:
        print "Error: %s" % e
        db.rollback()  
'''
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
'''
#@schedudler.cron_schedule(second='30', day_of_week='0-5', hour='9-12,13-15')
@schedudler.interval_schedule(minutes=5)
def say():
    saying=urllib.urlopen("http://www.verycd.com/statics/title.saying").read().decode('utf-8')
    #print saying
    subStr = saying[saying.find('y(')+2:saying.find(');')]
    db = MySQLdb.Connect("localhost","PECARD","PECARD","django",charset="utf8")
    cursor = db.cursor()
    #print subStr
    currenttime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for str in subStr.split("', '"):
        str_ = str.replace("'", "")
        print str_
        do_delete(cursor,db,str_)
        do_insert(cursor,db,str_,currenttime)
        
schedudler.start()
##
#sched.add_cron_job(say(),hour='17',minute='40',second='0')
