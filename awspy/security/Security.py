# -*- coding:utf-8 -*-
__author__ = 'artwebs'

import string
import struct

class Security(object):
     def getKey(self,key):
        rs=[0]*24
        num=0
        for i in range(24):
            if num>=len(key):
                num=0
            rs[i]=key[num]
            num+=1
        return ''.join(rs)
     def getIV(self,iv):
         rs=[0]*8
         num=0
         for i in range(8):
             if num>=len(iv):
                 num=0
             rs[i]=iv[num]
             num+=1
         return ''.join(rs)

     def nrPadBytes(self,blocksize, size):
        'Return number of required pad bytes for block of size.'
        if not (0 < blocksize < 255):
            raise NameError('blocksize must be between 0 and 255')
        return blocksize - (size % blocksize)

     def appendPadding(self,blocksize, s):
        '''Append rfc 1423 padding to string.

        RFC 1423 algorithm adds 1 up to blocksize padding bytes to string s. Each
        padding byte contains the number of padding bytes.
        '''
        n = self.nrPadBytes(blocksize, len(s))
        return s + (chr(n) * n)

     def removePadding(self,blocksize, s):
        'Remove rfc 1423 padding from string.'
        n = ord(s[-1]) # last byte contains number of padding bytes
        if n > blocksize or n > len(s):
            raise NameError('invalid padding')
        return s[:-n]