__author__ = 'artwebs'

from Crypto.Cipher import DES3
from Crypto import Random
from struct import *
import base64
from awspy.security.Security import *

class DESUtils(Security):
    def encode(self,key,source):
        key=self.getKey(key)
        iv = Random.new().read(DES3.block_size)
        cipher = DES3.new(key,DES3.MODE_CBC,iv)
        msg = iv+cipher.encrypt(source)
        msg=base64.encodestring(msg)
        return msg
    def decode(self,key,source):
        key =self.getKey(key)
        source=base64.decodestring(source)
        iv = Random.new().read(DES3.block_size)
        cipher = DES3.new(key, DES3.MODE_CBC,iv)
        msg =cipher.decrypt(source)
        return msg[8:len(msg)]

if __name__=="__main__":
    # ysedRi2FrlST+cQsk2DD4DphLQcvzpT6
    obj=DESUtils()
    rs=obj.encode("www.zcline.net","1103010900000013")
    print rs
    print obj.decode("www.zcline.net",rs)