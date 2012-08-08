'''
Created on 2010-10-30

@author: Administrator
'''

class LHBMap(object):
    __list=[]
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def put(self,key,value):
        dic={key:value}
        self.__list.append(dic)
        
    def getvalue(self,key=None,num=None):
        rs=None
        if key!=None or num!=None:
            for i in range(len(self.__list)):
                dic=self.__list[i]
                if key!=None:
                    if dic.has_key(key):
                        rs=dic.get(key)
                        break
                elif num!=None:
                    if num==i:
                        rs=(dic.values())[0]
                        break
                    
        return rs;
    
    def getkey(self,num=None):
        rs=None
        if num!=None:
            for i in range(len(self.__list)):
                dic=self.__list[i]
                if num!=None:
                    if num==i:
                        rs=(dic.keys())[0]
                        break
                    
        return rs;
    
    def setvalue(self,key=None,value=None,num=None):
        flag=False
        for i in range(len(self.__list)):
            dic=self.__list[i]
            if key!=None:
                if dic.has_key(key):
                    dic[key]=value
                    flag=True
                    break
            elif num!=None:
                if num==i:
                    key=(dic.keys())[0]
                    dic[key]=value
                    flag=True
                    break
        if not flag:
            self.put(key, value)
            
    def deletevalue(self,key=None,num=None):
         if key!=None or num!=None:
            for i in range(len(self.__list)):
                dic=self.__list[i]
                if key!=None:
                    if dic.has_key(key):
                        self.__list.pop(i)
                        break
                elif num!=None:
                    if num==i:
                        self.__list.pop(i)
                        break
    def isexists(self,key=None,num=None):
        flag=False
        if key!=None or num!=None:
            for i in range(len(self.__list)):
                dic=self.__list[i]
                if key!=None:
                    if dic.has_key(key):
                        flag=True
                        break
                elif num!=None:
                    if num==i:
                        flag=True
                        break
        return flag
                
    def getitem(self):
        return self.__list
    
    def clear(self):
        self.__list=[]
    
    def size(self):
        return len(self.__list)
            
def test():
    lm=LHBMap()
    lm.put("a", "1")
    lm.put("b", "2")
#    print lm.getvalue("a")
#    print lm.getvalue(None, 0)
    lm.setvalue("a", "3")
    lm.setvalue("d", "3")
    
    print lm.isexists("d")
    print lm.getitem()
    lm.deletevalue("d")
    print lm.getitem()
    
    
    
if __name__=="__main__":
    test()
    
    
    
    
        
        
        
        