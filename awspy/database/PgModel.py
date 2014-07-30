'''
Created on 2010-11-8

@author: Administrator
'''
import psycopg2
from awspy.database import DbModel,Db
from awspy.object import BinMap


class PgModel(DbModel):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None,port=None):
        Db.__init__(self,connstr,host,user,passwd,db,port)

    def getCursor(self):
        if self.port is not None:
            self.conn= psycopg2.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port,charset="utf8")
        else:
            self.conn= psycopg2.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=5432,charset="utf8")
        self.cursor = self.conn.cursor()