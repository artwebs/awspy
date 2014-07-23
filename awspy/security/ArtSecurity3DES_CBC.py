# -*- coding:utf-8 -*-
__author__ = 'artwebs'
from awspy.security.Security import Security
import pyDes
import base64


class ArtSecurity3DES_CBC(Security):
    def __init__(self):
        Security.__init__(self,2,24,8)

    def decode(self,source,key,iv="\0\0\0\0\0\0\0\0"):
        # obj=pyDes.des(self.getKey(key), pyDes.CBC,self.getIV(iv))
        obj=pyDes.triple_des(self.getKey(key), pyDes.CBC,self.getIV(iv))
        source=base64.decodestring(source)
        return obj.decrypt(source,padmode=pyDes.PAD_PKCS5)

    def encode(self,source,key,iv="\0\0\0\0\0\0\0\0"):
        # obj=pyDes.des(self.getKey(key), pyDes.CBC, self.getIV(iv))
        obj=pyDes.triple_des(self.getKey(key), pyDes.CBC, self.getIV(iv))
        return base64.encodestring(obj.encrypt(source,padmode=pyDes.PAD_PKCS5))

if __name__=="__main__":
    obj=ArtSecurity3DES_CBC()
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

