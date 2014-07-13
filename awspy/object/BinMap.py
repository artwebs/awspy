# -*- coding: utf-8 -*-
'''
Created on 2010-10-30

@author: Administrator
'''

class BinMap(object):
    __keys=[]
    __values=[]
    '''
    classdocs
    '''


    def __init__(self):
        self.__keys=[]
        self.__values=[]
        '''
        Constructor
        '''
        
    def put(self,key,value):
        self.__values.append(value)
        self.__keys.append(key)
        
    def getvalue(self,key=None,num=None):
        rs=None
        if key!=None and key in self.__keys:
            rs=self.__values[self.__keys.index(key)]
        elif num!=None and num<len(self.__keys):
            rs=self.__values[num]                  
        return rs;
    
    def getkey(self,num=None):
        rs=None
        if num!=None:
            rs=self.__keys[num]                    
        return rs;
    
    def setvalue(self,key=None,value=None,num=None):
        flag=False
        if key!=None and key in self.__keys:
            self.__values[self.__keys.index(key)]=value           
        elif num!=None and num <len(self.__keys):
            self.values[num]=value   
        if not flag:
            self.put(key, value)
            
    def deletevalue(self,key=None,num=None):
        flag=True
        if key!=None and key in self.__keys:
            self.__values[self.__keys.index(key)]=[]
            self.__keys[self.__keys.index(key)]=[]
        elif num!=None and num<len(self.__keys):
            self.__values[num]=[]
            self.__keys[num]=[]
        else :
            flag=False
             
    def isexists(self,key=None,num=None):
        flag=False
        if key!=None and key in self.__keys:
           flag=True          
        elif num!=None and num<len(self.__keys):
           flag=True
        return flag
                
    def getitem(self):
        return dict(zip(self.__keys,self.__values))
    
    def getkeys(self):
        return self.__keys;
    
    def getvalus(self):
        return self.__values;
    
    def clear(self):
        self.__keys=[]
        self.__values=[]
    
    def size(self):
        return len(self.__keys)
    
    
if __name__=="__main__":
    test()
    
    
    
    
        
        
        
        