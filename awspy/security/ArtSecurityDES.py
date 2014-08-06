# -*- coding:utf-8 -*-
from awspy.security.Security import Security
from awspy.security import pyDes

__author__ = 'artwebs'
import base64

DES=1
TRIPLEDES=2

# Modes of crypting / cyphering
ECB =	0
CBC =	1

# Modes of padding
PAD_NORMAL = 1
PAD_PKCS5 = 2

class ArtSecurityDES(Security):
    __action=None
    __model=None
    __padmodel=None
    def __init__(self,act=TRIPLEDES,mod=ECB,padmod=PAD_PKCS5):
        self.__action=act
        self.__model=mod
        self.__padmodel=padmod
        if  self.__action==TRIPLEDES:
            Security.__init__(self,24,8)
        else:
            Security.__init__(self,8,8)

    def decode(self,source,key,iv="\0\0\0\0\0\0\0\0"):
        if self.__action==TRIPLEDES:
            obj= pyDes.triple_des(self.getKey(key), self.__model,self.getIV(iv))
        else:
            obj= pyDes.des(self.getKey(key), self.__model,self.getIV(iv))
        source=base64.decodestring(source)
        return obj.decrypt(source,padmode=self.__padmodel)

    def encode(self,source,key,iv="\0\0\0\0\0\0\0\0"):
        # obj=pyDes.des(self.getKey(key), pyDes.CBC, self.getIV(iv))
        if self.__action==TRIPLEDES:
            obj= pyDes.triple_des(self.getKey(key), self.__model, self.getIV(iv))
        else:
            obj= pyDes.des(self.getKey(key), self.__model, self.getIV(iv))
        return base64.encodestring(obj.encrypt(source,padmode=self.__padmodel))

def __testTRIPLEDES():
    print "===============TRIPLEDES================"
    objECB=ArtSecurityDES()
    key="www.zcline.net"
    text="a12*&1c中文"
    rs=objECB.encode(text,key)

    print 'DEC_ECB generateSecretKey:'+objECB.generateSecretKey()
    print("ts7JDFmRRIX8vIpfOc6s6A==")
    print(rs)
    print(text)
    print (objECB.decode(rs,key))

    key="www.zcline.net"
    text="1103010900000013"
    rs=objECB.encode(text,key)
    print "ysedRi2FrlST+cQsk2DD4DphLQcvzpT6"
    print rs
    print text
    print objECB.decode(rs,key)


    objEBC=ArtSecurityDES(mod=CBC)
    print 'DEC_CBC generateSecretKey:'+objEBC.generateSecretKey()
    key="www.zcline.net"
    text="a12*&1c中文"
    iv="artwebs"
    rs=objEBC.encode(text,key,iv)
    print("ts7JDFmRRIX8vIpfOc6s6A==")
    print(rs)
    print(text)
    print (objEBC.decode(rs,key,iv))

    key="www.zcline.net"
    text="1103010900000013"
    rs=objEBC.encode(text,key,iv)
    print "bXgKYTR47dosKznX/32ARzoeuuBsdfIn"
    print rs
    print text
    print objEBC.decode(rs,key,iv)

def __testDES():
    print "===============DES================"
    objECB=ArtSecurityDES(act=DES)
    key="www.zcline.net"
    text="a12*&1c中文"
    rs=objECB.encode(text,key)

    print("ts7JDFmRRIX8vIpfOc6s6A==")
    print(rs)
    print(text)
    print (objECB.decode(rs,key))

    key="www.zcline.net"
    text="1103010900000013"
    rs=objECB.encode(text,key)
    print "6TgFnBfUBNXc8hH4+zYYRqOgOw0X5iPU"
    print rs
    print text
    print objECB.decode(rs,key)


    objEBC=ArtSecurityDES(act=DES,mod=CBC)
    key="www.zcline.net"
    text="a12*&1c中文"
    iv="artwebs"
    rs=objEBC.encode(text,key,iv)

    print("ts7JDFmRRIX8vIpfOc6s6A==")
    print(rs)
    print(text)
    print (objEBC.decode(rs,key,iv))

    key="www.zcline.net"
    text="1103010900000013"
    rs=objEBC.encode(text,key,iv)
    print "6EWe/6/qf3XbN4Wm6KKoBA=="
    print rs
    print text
    print objEBC.decode(rs,key,iv)

if __name__=="__main__":
    __testTRIPLEDES()
    __testDES()




