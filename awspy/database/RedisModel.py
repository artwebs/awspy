# -*- coding: utf-8 -*-
__author__ = 'liuhongbin'
import awspy.database.redisco
from redisco import models
from awspy.database.DbModel import DbModel
from awspy.object.BinMap import BinMap
from awspy.object.BinList import BinList
class RedisModel(DbModel):
    def __init__(self,tablename=None):
        if tablename is not None: self.__tablename=tablename

    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None,port=None):
        DbModel.__init__(self,connstr,host,user,passwd,db,port)

    def getCursor(self):
        pass
        # if self.port is not None:
        #     self.conn= redis.Redis(host=self.host, port=self.port, db=self.db)
        # else:
        #     self.conn= redis.Redis(host=self.host, port=6379, db=self.db)
        # print(self.conn.mget('foo','c2'))
        # print 'incr:',self.conn.incr('a')
        # print str(self.conn.lastsave('foo'))


class Person(models.Model):
    name = models.Attribute(required=True)
    created_at = models.DateTimeField(auto_now_add=True)
    fave_colors = models.ListField(str)

if __name__=="__main__":
    # db=RedisModel(host='127.0.0.1', db=0)
    # db.getCursor()
    # person = Person(name="Conchita")
    # print person.is_valid()
    # person.delete()
    # person.save()
    conchita = Person.objects.filter(name='Conchita')
    print(conchita[0].id)

    # Person.objects.create(name="Conchita")
    # for person in Person.objects.all():
    #         person.delete()
