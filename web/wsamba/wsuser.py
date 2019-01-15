#!/usr/bin/env python
#coding:utf8

import os
import logging
from subprocess import PIPE,Popen

logger = logging.getLogger('django')


class wsuser(object):
    def __init__(self,name,pwd=None,lock=False,unlock=True):
        self._name = name
        self._pwd = pwd
        self.Lock = lock
        self.Unlock = unlock

        global err
        cmd = """ grep -w  %s /etc/passwd ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%self._name
        data = Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
        err = data.stderr.read()
        if err:
            logger.error(err)
            return 

    def wuadd(self):
        self._cmd = """echo -e '%s\n%s' |smbpasswd -s -a %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%(self._pwd,self._pwd,self._name)
        data = Popen(self._cmd,shell=True,stderr=PIPE,stdout=PIPE)
        err = data.stderr.read()
        if err:
            logger.error(err)
        else:
            logger.info('SAMBA USER:'+self._name +'was added.')
    
    def wudel(self):
        self._cmd = """pdbedit -x %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%self._name
        data = Popen(self._cmd,shell=True,stderr=PIPE,stdout=PIPE)
        err = data.stderr.read()
        if err:
            logger.error(err)
        else:
            logger.info('SAMBA USER:'+  self._name +'  was deleted.')

    def wupause(self):
        self._cmd = """smbpasswd -d %s; if [ $? -ne 0 ];then echo 1 >&2;fi"""%self._name
        data = Popen(self._cmd,shell=True,stderr=PIPE,stdout=PIPE)
        err = data.stderr.read()
        if err:
            logger.error(err)
        else:
            logger.info('SAMBA USER:'+self._name +'was stoped.')
        
    def wuenable(self):
        self._cmd = """smbpasswd -e %s; if [ $? -ne 0 ];then echo 1 >&2;fi"""%self._name
        data = Popen(self._cmd,shell=True,stderr=PIPE,stdout=PIPE)
        err = data.stderr.read()
        if err:
            logger.error(err)
        else:
            logger.info('SAMBA USER:'+self._name +'was enabled.')

if __name__ == '__main__':
    Choice = input('请选择操作：1 添加、2 删除、3 修改、4 禁用、5 启用:')
    if type(Choice) != int:
       exit(1) 
    name = input('Please input 用户名:')
    pwd1 = input('Please input 密钥:')
    pwd2 = input('Please reinput 密钥:')
    if pwd1 == pwd2:
        pwd = pwd1
        user = wsuser(name,pwd)
        if err:
            print("user not in system. Please create user first.")
        else: 
            user.wuadd()

