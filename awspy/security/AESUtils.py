# -*- coding:utf-8 -*-
__author__ = 'artwebs'

from Crypto.Cipher import AES
from Crypto import Random
from struct import *
import base64
from awspy.security.Security import *

class  AESUtils(Security):
    def encode(self,key,source):
        key=self.getKey(key)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key,AES.MODE_CBC,iv)
        msg = iv+cipher.encrypt(source)
        msg=base64.encodestring(msg)
        return msg
    def decode(self,key,source):
        key =self.getKey(key)
        source=base64.decodestring(source)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC,iv)
        msg =cipher.decrypt(source)
        return msg[16:len(msg)]


if __name__=="__main__":
    obj=AESUtils()
    rs=obj.encode("www.zcline.net","1103010900000013")
    print rs
    print obj.decode("www.zcline.net",rs)