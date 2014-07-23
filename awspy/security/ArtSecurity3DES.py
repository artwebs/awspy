# -*- coding:utf-8 -*-
__author__ = 'artwebs'

from Crypto.Cipher import DES3
from Crypto import Random
import base64
from awspy.common.Method import *
from awspy.security.Security import *


class ArtSecurity3DES(Security):
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
        import random
        import struct
        import hashlib
        seeds = random.random()
        m = hashlib.md5()
        m.update(str(seeds))
        ret1 = m.digest()
        seeds = random.random()
        m.update(str(seeds))
        ret2 = m.digest()
        ret = struct.pack("%ds%ds"%(len(ret1),len(ret2)),ret1,ret2)
        return ret

    def randomIVBytes(self):
        return Random.new().read(DES3.block_size)





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