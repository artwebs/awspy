# -*- coding: utf-8 -*-
'''
Created on 2010-11-8

@author: Administrator
'''
import psycopg2
from awspy.database.DbModel import DbModel
from awspy.object.BinMap import BinMap
from awspy.object.BinList import BinList

class PgModel(DbModel):
    '''
    classdocs
    '''

    def __init__(self,tablename=None):
        if tablename is not None: self.__tablename=tablename

    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None,port=None):
        DbModel.__init__(self,connstr,host,user,passwd,db,port)

    def getCursor(self):
        if self.port is not None:
            self.conn= psycopg2.connect(host=self.host,user=self.user,password=self.passwd,database=self.db,port=self.port)
        else:
            self.conn= psycopg2.connect(host=self.host,user=self.user,password=self.passwd,database=self.db,port=5432)
        self.cursor = self.conn.cursor()

if __name__=="__main__":
    import json
    db=PgModel(host='127.0.0.1', user='postgres',passwd='windows123',db='awsweb')
    f= BinMap();
    # f.put("login_name","")
    # f.put("user_name","")
    # print (db.getSelectResult(f,'1=1','pu_user')).getitem()

    # f.clear()
    # f.put("v_json","")
    # f.put("v_code","")
    # f.put("v_message","")
    # rs=db.getSelectResult(f,'1=1','validate_user(\'admin\',\' v_pwd\',null,null,\'web\')')
    # print rs.getitem()

    f.put("ojson","")
    rs=db.getSelectResult(f,'1=1','aws_entrance(\'validate_user\',\'admin\')')
    print json.loads(rs.getvalue(0,"ojson"))

    # db.getCursor()
    #
    # db.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    # db.cursor.callproc("validate_user", ['admin',' v_pwd',None,None,'web'])
    # print db.cursor.fetchone()
    # db.cursor.execute ( "fetch", [ "_ref" ] ) # fetch row from this cursor
    # db.cursor.fetchone()
    # # cur2 = db.cursor()
    # print cur2.fetchone()
    # db.closeCursor()

    # db.getCursor()
    # db.cursor.callproc("reffunc", ['curname'])
    # cur2 = db.conn.cursor('curname')
    # print cur2.fetchone()