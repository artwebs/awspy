# -*- coding:utf-8 -*-
__author__ = 'artwebs'

from Crypto.Cipher import DES3
from Crypto import Random
import base64
from awspy.common.Method import *
from awspy.security.Security import *


class ArtSecurity3DES(Security):

    def __init__(self):
        Security.__init__(self,DES3.MODE_CBC,DES3.key_size[1],DES3.block_size)

    def encode(self,source,key,iv):
        key=self.getKey(key,self.keysize)
        cipher = DES3.new(key,self.mode,self.getIV(iv,self.blocksize))
        msg = cipher.encrypt(self.appendPadding(self.blocksize,source))
        msg=base64.encodestring(msg)
        return msg
    def decode(self,source,key,iv):
        key =self.getKey(key,self.keysize)
        source=base64.decodestring(source)
        cipher = DES3.new(key, self.mode,self.getIV(iv,self.blocksize))
        msg =cipher.decrypt(source)
        return msg


if __name__=="__main__":
    obj=ArtSecurity3DES()
    print("generateSecretKey:",str(obj.generateSecretKey()).encode('hex'))
    print("randomIVBytes:",str(obj.randomIVBytes()).encode('hex'))
    key="www.zcline.net"
    iv="artwebs"
    text="a12*&1c中文"
    rs=obj.encode(text,key,iv)
    print("ts7JDFmRRIX8vIpfOc6s6A==")
    print(rs)
    print(text)
    print (obj.decode(rs,key,iv))


    key="www.zcline.net"
    iv="\0\0\0\0\0\0\0\0"
    text="1103010900000013"
    rs=obj.encode(text,key,iv)
    print("ysedRi2FrlST+cQsk2DD4DphLQcvzpT6")
    print(rs)
    print(text)
    print (obj.decode(rs,key,iv))