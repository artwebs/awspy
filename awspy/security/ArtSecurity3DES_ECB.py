# -*- coding:utf-8 -*-
__author__ = 'artwebs'
from awspy.security.Security import Security
import pyDes
import base64

class ArtSecurity3DES_ECB(Security):
    def __init__(self):
        Security.__init__(self,2,24,8)

    def decode(self,source,key):
        obj=pyDes.triple_des(self.getKey(key))
        source=base64.decodestring(source)
        return obj.decrypt(source,padmode=pyDes.PAD_PKCS5)

    def encode(self,source,key):
        obj=pyDes.triple_des(self.getKey(key))
        return base64.encodestring(obj.encrypt(source,padmode=pyDes.PAD_PKCS5))

if __name__=="__main__":
    obj=ArtSecurity3DES_ECB()
    key="www.zcline.net"
    text="a12*&1c中文"
    rs=obj.encode(text,key)
    print obj.randomIVBytes()
    print obj.generateSecretKey()

    print("ts7JDFmRRIX8vIpfOc6s6A==")
    print(rs)
    print(text)
    print (obj.decode(rs,key))

    key="www.zcline.net"
    text="1103010900000013"
    rs=obj.encode(text,key)
    print "ysedRi2FrlST+cQsk2DD4DphLQcvzpT6"
    print rs
    print text
    print obj.decode(rs,key)

