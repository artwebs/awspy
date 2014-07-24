# -*- coding:utf-8 -*-
__author__ = 'artwebs'
from awspy.security.Security import Security
import pyDes
import base64

# Modes of crypting / cyphering
ECB =	0
CBC =	1

# Modes of padding
PAD_NORMAL = 1
PAD_PKCS5 = 2

class ArtSecurity3DES_CBC(Security):
    __model=None
    __padmodel=None
    def __init__(self,mod=ECB,padmod=PAD_PKCS5):
        self.__model=mod
        self.__padmodel=padmod
        Security.__init__(self,24,8)

    def decode(self,source,key,iv="\0\0\0\0\0\0\0\0"):
        # obj=pyDes.des(self.getKey(key), pyDes.CBC,self.getIV(iv))
        obj=pyDes.triple_des(self.getKey(key), self.__model,self.getIV(iv))
        source=base64.decodestring(source)
        return obj.decrypt(source,padmode=self.__padmodel)

    def encode(self,source,key,iv="\0\0\0\0\0\0\0\0"):
        # obj=pyDes.des(self.getKey(key), pyDes.CBC, self.getIV(iv))
        obj=pyDes.triple_des(self.getKey(key), self.__model, self.getIV(iv))
        return base64.encodestring(obj.encrypt(source,padmode=self.__padmodel))

if __name__=="__main__":
    objECB=ArtSecurity3DES_CBC()
    key="www.zcline.net"
    text="a12*&1c中文"
    rs=objECB.encode(text,key)
    print objECB.randomIVBytes()
    print objECB.generateSecretKey()

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


    obj=ArtSecurity3DES_CBC(CBC)
    key="www.zcline.net"
    text="a12*&1c中文"
    iv="artwebs"
    rs=obj.encode(text,key,iv)
    print("ts7JDFmRRIX8vIpfOc6s6A==")
    print(rs)
    print(text)
    print (obj.decode(rs,key,iv))

    key="www.zcline.net"
    text="1103010900000013"
    rs=obj.encode(text,key,iv)
    print "bXgKYTR47dosKznX/32ARzoeuuBsdfIn"
    print rs
    print text
    print obj.decode(rs,key,iv)

