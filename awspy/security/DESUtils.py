# -*- coding:utf-8 -*-
__author__ = 'artwebs'

from Crypto.Cipher import DES3
from Crypto import Random
import base64
from awspy.common.Method import *
from awspy.security.Security import *


class DESUtils(Security):
    def encode(self,source,key,iv):
        key=self.getKey(key)
        cipher = DES3.new(key,DES3.MODE_CBC,self.getIV(iv))
        msg = cipher.encrypt(self.appendPadding(DES3.block_size,source))
        msg=base64.encodestring(msg)
        return msg
    def decode(self,source,key,iv):
        key =self.getKey(key)
        source=base64.decodestring(source)
        cipher = DES3.new(key, DES3.MODE_CBC,self.getIV(iv))
        msg =cipher.decrypt(source)
        return msg

    def  generateSecretKey(self):
        return Random.new.read(DES3.MODE_CBC)

    def randomIVBytes(self):
        return Random.new().read(DES3.block_size)





if __name__=="__main__":
    obj=DESUtils()
    key="www.zcline.net"
    iv="artwebs"
    text="1103010900000013"
    rs=obj.encode(text,key,iv)
    print(rs)
    print obj.decode(rs,key,iv)
    print obj.decode("bXgKYTR47dosKznX/32ARzoeuuBsdfIn",key,iv)
    print obj.decode("bXgKYTR47dosKznX/32ARw==",key,iv)

    print(base64.decodestring("RzoeuuBsdfIn"))