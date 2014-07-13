#coding=utf-8
import unittest

from awspy.action.ActionXml import *
from awspy.object.BinMap import *
from awspy.object.BinList import *


class Test(unittest.TestCase):
    

    def testGetList(self):
        data=BinList();
        data.put(0,'name','张三');
        data.put(0, 'sex', '男');
        data.put(0, 'id', '1');
        data.put(1,'name','李四');
        data.put(1, 'sex', '女');
        data.put(1, 'id', '2');
        
        para=BinMap();
        para.put("text", '[name],[sex]');
        para.put('id','[id]');
        
        obj=ActionXml();
        obj.getList(data, para, None);
        self.assertEqual(obj.reponse(),'<?xml version="1.0" encoding="utf-8"?><root><message>数据下载成功</message><code>1</code><count>2</count><data><row><text>张三,男</text><id>1</id></row><row><text>李四,女</text><id>2</id></row></data></root>')
    
    
    def testGetResult(self):
        args=BinMap()
        args.put("message", '更新成功')
        obj=ActionXml();
        obj.getResult(args)
        self.assertEqual(obj.reponse(),'<?xml version="1.0" encoding="utf-8"?><root><message>更新成功</message><code>1</code></root>')
    
    def testGetInfo(self):
        data=BinList();
        data.put(0,'name','张三');
        data.put(0, 'sex', '男');
        data.put(0, 'id', '1');
        data.put(1,'name','李四');
        data.put(1, 'sex', '女');
        data.put(1, 'id', '2');
        items=BinMap();
        items.put("name", "姓名");
        items.put("sex", "性别");
        items.put("id", "编号");
        args=BinMap();
        args.put("message", '更新');
        obj=ActionXml();
        obj.getInfo(data, items, args);
#        self.assertAlmostEqual(obj.reponse(),'<?xml version="1.0" encoding="utf-8"?><root><message>更新</message><code>1</code><count>2</count><data><row>【编号】1\n【姓名】张三\n【性别】男</row><row>【编号】2\n【姓名】李四\n【性别】女</row></data></root>')
        print obj.reponse();

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()