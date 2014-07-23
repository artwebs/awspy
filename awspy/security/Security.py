# -*- coding:utf-8 -*-
__author__ = 'artwebs'

import string
import struct
from Crypto import Random

class Security(object):
     mode=None
     keysize=None
     blocksize=None

     def __init__(self,mod,ksize,bsize):
         self.mode=mod
         self.keysize=ksize
         self.blocksize=bsize

     def getKey(self,key,ksize):
        rs=[0]*ksize
        num=0
        for i in range(ksize):
            if num>=len(key):
                num=0
            rs[i]=key[num]
            num+=1
        return ''.join(rs)
     def getIV(self,iv,bsize):
         rs=[0]*bsize
         num=0
         for i in range(bsize):
             if num>=len(iv):
                 num=0
             rs[i]=iv[num]
             num+=1
         return ''.join(rs)

     def nrPadBytes(self,bsize, size):
        'Return number of required pad bytes for block of size.'
        if not (0 < bsize < 255):
            raise NameError('blocksize must be between 0 and 255')
        return bsize - (size % bsize)

     def appendPadding(self,bsize, s):
        '''Append rfc 1423 padding to string.

        RFC 1423 algorithm adds 1 up to blocksize padding bytes to string s. Each
        padding byte contains the number of padding bytes.
        '''
        n = self.nrPadBytes(bsize, len(s))
        return s + (chr(n) * n)

     def removePadding(self,bsize, s):
        'Remove rfc 1423 padding from string.'
        n = ord(s[-1]) # last byte contains number of padding bytes
        if n > bsize or n > len(s):
            raise NameError('invalid padding')
        return s[:-n]



     def randomBytes(self,bsize):
        return Random.new().read(bsize)


     def  generateSecretKey(self):
        return self.randomBytes(self.keysize)

     def randomIVBytes(self):
        return self.randomBytes(self.blocksize)