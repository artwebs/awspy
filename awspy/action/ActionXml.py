# -*- coding: utf-8 -*-
import re
import xml.dom.minidom

from awspy.object.BinMap import BinMap
from awspy.action.Action import *


class ActionXml(Action):
    __dom=None;
    __root=None;
    __args=None;

    def __init__(self):
        self.init();
        
    def getList(self,data,items,args=None):
        self.appendAttribute("type", "list")
        args.put('count',str(data.size()))
        self.initArgs(args);
        rows=self.appendElement('list')
        for i in range(0,data.size()):
            row=self.appendElement('item')
            for j in range(0,items.size()):
                yitem=str(items.getvalue(num=j))
                p = re.compile(r'\[(\w+)\]')
                for m in p.finditer(yitem):
                    yitem=yitem.replace(str(m.group()),str(data.getvalue(i,str(m.group(1)))))
                self.appendElement(items.getkey(num=j),yitem,row)
            rows.appendChild(row)
        self.__root.appendChild(rows)
        
    def getPageList(self,data,items,args=None):
        self.appendAttribute('type', 'pagelist')
        rowsCount=data.getvalue(key='rowsCount')
        rowsData=data.getvalue(key="rows")
        args.put('count',str(rowsCount))
        self.initArgs(args);
        rows=self.appendElement('list')
        for i in range(0,rowsData.size()):
            row=self.appendElement('item')
            for j in range(0,items.size()):
                yitem=str(items.getvalue(num=j))   
                p = re.compile(r'\[(\w+)\]')
                for m in p.finditer(yitem):
                    yitem=yitem.replace(str(m.group()),str(rowsData.getvalue(i,str(m.group(1)))))                
                self.appendElement(items.getkey(num=j),yitem,row)           
            rows.appendChild(row)
        self.__root.appendChild(rows)
        
        
    def getResult(self,args):
        self.initArgs(args);
        
    def getInfo(self,data,items,args=None):
        self.appendAttribute('type', 'info')
        args.put('count',str(data.size()))
        self.initArgs(args);
        rows=self.appendElement('list')
        for i in range(0,data.size()):
            content="";
            for j in range(0,items.size()):
                content+="【"+items.getvalue(num=j)+"】"+data.getvalue(i,items.getkey(j));     
                if j is not items.size()-1:
                    content+="\n";
            self.appendElement("item", content, rows)
        self.__root.appendChild(rows)
        
    def init(self):
        impl = xml.dom.minidom.getDOMImplementation()
        self.__dom=impl.createDocument(None, "doc", None)
        self.__root=self.__dom.documentElement
        
    def initArgs(self,args):
        self.__args=args;
        if self.__args is None:
            self.__args=BinMap()
            self.__args.put('code', '1');
            self.__args.put('message', '数据下载成功');
        else:
            if not self.__args.isexists('code'):
                self.__args.put('code', '1');
            if not self.__args.isexists('message'):
                self.__args.put('message', '数据下载成功');
            if not self.__args.isexists('count'):
                self.__args.put('count', '0');
        
        for i in range(0,self.__args.size()):
            self.appendElement(self.__args.getkey(i), self.__args.getvalue(num=i))
            
    def appendElement(self,item,text=None,parent=None):
        element=self.__dom.createElement(item);
        if text is not None:
            text=self.__dom.createTextNode(text);
            element.appendChild(text);
        if parent is None:
            self.__root.appendChild(element);
        else:
            parent.appendChild(element);
        return element;
    
    def appendAttribute(self,key,value,element=None):
        if element is not None:
            element.setAttribute(key, value)
        else:
            self.__root.setAttribute(key, value)
    
    def reponse(self):
        return self.__dom.toxml('utf-8');