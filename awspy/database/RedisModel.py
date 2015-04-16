# -*- coding: UTF-8 -*-
__author__ = 'liuhongbin'
from awspy.database.redisco import *
from awspy.database.redisco import models
from awspy.database.DbModel import DbModel
class RedisModel(DbModel):
    def __init__(self,tablename=None):
        if tablename is not None: self.__tablename=tablename

    def __init__(self,connstr=None,host=None,user=None,passwd=None,db=None,port=None):
        DbModel.__init__(self,connstr,host,user,passwd,db,port)
        # {'host': 'localhost','port': 6379, 'db': 0}
        connection_setup(host=self.host,port=self.port,db=self.db)

    #talbe 表名
    #kwargs filter 不传的时候查询全部 order limit
    def select_object_list(self,table,**kwargs):
        rs_list=[]
        filter=None
        order=None
        limit=None
        page=None
        pagesize=None
        for key in kwargs:
            if key=='filter':
                filter=kwargs[key]
            elif key=='order':
                order=kwargs[key]
            elif key=='limit':
                limit=kwargs[key]
            elif key=='page':
                page=int(kwargs[key])
            elif key=='pagesize':
                pagesize=int(kwargs[key])
        if limit is None and page is not None and pagesize is not None:
            limit=[pagesize,(page-1)*pagesize]
        print filter,order,limit
        if filter is not None:
            if set(["id"]).issubset(filter):
                obj_list=[]
                for id in filter["id"].split(','):
                    obj_list.append(table.objects.get_by_id(id))
            else:
                obj_list=table.objects.filter(**filter)
        else:
            obj_list=table.objects.all()

        if order is not None:
            obj_list=obj_list.order(*order)
        if limit is not None:
            obj_list=obj_list.limit(*limit)
        return obj_list

    #talbe 表名
    #args 返回字段
    #kwargs filter 不传的时候查询全部 order limit
    def select(self,table,*args,**kwargs):
        rs_list=[]
        obj_list=self.select_object_list(table,**kwargs)
        for row in obj_list:
            if row is None:
                continue
            s_row={'id':row.id}
            if len(args)>0:
                for filed in args:
                    s_row[filed]=str(getattr(row,filed))
            else:
                attrs = row.attributes.values() + row.lists.values() \
                + row.references.values()
                for att in attrs:
                   s_row[att.name]=str(getattr(row,att.name))
            rs_list.append(s_row)
        return rs_list

    #kwargs 插入字段
    def insert(self,table,**kwargs):
        obj=table(**kwargs)
        return obj.save()

    #kwargs 修改字段及值及同select的filter
    def update(self,table,**kwargs):
        filter=None
        field_dic={}
        for key in kwargs:
            if key=='filter':
                filter=kwargs[key]
            else:
                field_dic[key]=kwargs[key]
        obj_list=self.select_object_list(table,**filter)
        for row in obj_list:
            for field in field_dic:
                setattr(row, field, field_dic[field])
            row.save()
        return True

    #kwargs 同select的filter
    def delete(self,table,**kwargs):
        filter=None
        for key in kwargs:
            if key=='filter':
                filter=kwargs[key]
        if filter is not None:
            obj_list=self.select_object_list(table,**filter)
        else:
            obj_list=self.select_object_list(table)
        for row in obj_list:
            row.delete()
        return True

if __name__=="__main__":
    class Person(models.Model):
        name = models.Attribute(required=True)
        created_at = models.DateTimeField(auto_now_add=True)
        fave_colors = models.ListField(str)
    db=RedisModel(host='localhost', port=6379,db=0)
    print db.insert(Person,name='Conchita4')
    print db.select(Person,'name','created_at','fave_colors')
    #print db.select(Person,'name','created_at','fave_colors',filter={"name":'Conchita4'},order=['-created_at'],limit=[2,0])
    #print db.select(Person,'name','created_at','fave_colors',filter={"id":"21"})
    #print db.select(Person,'name','created_at','fave_colors',filter={"id":"21,22"})

    # db.update(Person,name='Conchita0',filter={"id":"21,22"})
    # print db.select(Person,'name','created_at','fave_colors',filter={"id":"21,22"})
    #
    # db.delete(Person,name='Conchita0',filter={"id":"21,22"})
    # print db.select(Person,'name','created_at','fave_colors',filter={"id":"21,22"})

