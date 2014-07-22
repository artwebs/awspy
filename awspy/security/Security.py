__author__ = 'artwebs'

class Security(object):
     def getKey(self,key):
        rskey="";
        for i in range(24):
            if i<len(key):
                rskey+=key[i]
            else :
                rskey+="0"
        return rskey;
