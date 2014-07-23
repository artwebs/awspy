# -*- coding:utf-8 -*-
__author__ = 'artwebs'

from Crypto.Cipher import AES
from Crypto import Random
from struct import *
import base64
from awspy.security.Security import *

class  ArtSecurityAES(Security):
    def __init__(self):
        Security.__init__(self,AES.MODE_CBC,AES.key_size[1],AES.block_size)

    def encode(self,source,key,iv):
        key=self.getKey(key,self.keysize)
        cipher = AES.new(key,self.mode,iv)
        msg = iv+cipher.encrypt(source)
        msg=base64.encodestring(msg)
        return msg
    def decode(self,source,key,iv):
        key =self.getKey(key,self.keysize)
        source=base64.decodestring(source)
        cipher = AES.new(key, self.mode,iv)
        msg =cipher.decrypt(source)
        return msg[16:len(msg)]


if __name__=="__main__":
    obj=ArtSecurityAES()
    iv=obj.randomIVBytes()

    print("generateSecretKey:",str(obj.generateSecretKey()).encode('hex'))
    print("randomIVBytes:",str(obj.randomIVBytes()).encode('hex'))
    rs=obj.encode("1103010900000013","www.zcline.net",iv)
    print rs
    print obj.decode(rs,"www.zcline.net",iv)