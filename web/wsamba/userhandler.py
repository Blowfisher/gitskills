#!/usr/bin/env python
#coding:utf8

import os,sys
import logging
from subprocess import Popen,PIPE
import argparse

logger = logging.getLogger('django')


def dpt_add(dptname):
    dcmd = """groupadd %s;if [ $? -ne 0 ];then echo 1 >&2;fi"""%dptname
    ddata = Popen(dcmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = ddata.stderr.read()
    if error:
        logger.error(error)
        return
    else:
        logger.warning('Department :'+dptname+'was added.')
        return

def dpt_del(dptname):
    dcmd = """groupdel %s;if [ $? -ne 0 ];then echo 1 >&2;fi"""%dptname
    ddata = Popen(dcmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = ddata.stderr.read()
    if error:
        logger.error(error)
        return
    else:
        logger.warning('Department :'+dptname+'was deleted.')
        return   
 
def admin_add(username):
    acmd = """useradd -M -s /sbin/nologin %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%username
    adata = Popen(acmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = adata.stderr.read()
    if error:
        logger.error(error)
        return
    else:
        logger.info('User was created.')
        return   

def com_add(username,group):
    ccmd = """useradd -M -s /sbin/nologin -G %s %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%(group,username)
    cdata = Popen(ccmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = cdata.stderr.read()
    if error:
        logger.error(error)
        return
    else:
        logger.info('User was created.')
        return   

def user_del(username):
    dcmd = """userdel -r %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%username
    ddata = Popen(dcmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = ddata.stderr.read()
    if error:
        logger.error(error)
        return
    else:
        logger.warning('User was deleted.')
        return   

def cgroup(username,args):
    data = args
    for i in data:
        group += str(i)+','
    group = group.strip(',')
    cgcmd = """usermod -G %s %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%(group,username)
    cgdata = Popen(cgcmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = cgdata.stderr.read()
    if error:
        logger.error(error)
        return
    else:
        logger.warning('Group was changed.')
        return   
    

def user_mod(username,pwd=None,login_name=None,group=None,lock=None,unlock=None):
    def cpwd(username,pwd):
        pcmd = """usermod -p %s %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%(pwd,username)
        pdata = Popen(pcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = pdata.stderr.read()
        if error:
            logger.error(error)
            return
        else:
            logger.warning(username + ' password was changed.')
            return   

    def cname(username,login_name):
        cncmd = """usermod -l %s %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%(login_name,username)
        cndata = Popen(cncmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = cndata.stderr.read()
        if error:
            logger.error(error)
            return
        else:
            logger.warning(username + 'name was changed.')
            return   

    def cgroup(username,group):
        cgcmd = """usermod -g %s %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%(group,username)
        cgdata = Popen(cgcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = cgdata.stderr.read()
        if error:
            logger.error(error)
            return
        else:
            logger.warning('Group was changed.')
            return   
   
    def locker(username):
        lcmd = """usermod -L %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%username
        ldata = Popen(lcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = ldata.stderr.read()
        if error:
            logger.error(error)
            return
        else:
            logger.warning(username + ' was locked.')
            return   
   
    def ulocker(username):
        ulcmd = """usermod -U %s ;if [ $? -ne 0 ];then echo 1 >&2;fi"""%username
        uldata = Popen(ulcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = uldata.stderr.read()
        if error:
            logger.error(error)
            return
        else:
            logger.warning(username + ' was unlocked.')
            return   
    if pwd:
        cpwd(username,pwd)
    if login_name:
        cname(username,login_name)
    if group:
        cgroup(username,group)
    if lock:
        locker(username)
    if unlock:
        ulocker(username)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--username',dest='username',nargs='?',help="username is Need.")
    parser.add_argument('--admin',action='store_true',help="username is admin.")
    parser.add_argument('--common',action='store_true',help="username is comon.")
    parser.add_argument('--delete',action='store_true',help="Dek username.")
    parser.add_argument('-g','--group',dest='group',nargs='?',help="Change group of username.")
    parser.add_argument('-p','--passwd',dest='pwd',nargs='?',help="Set the password of username.")
    parser.add_argument('-n','--login_name',dest='login_name',nargs='?',help="Change the name of username.")
    parser.add_argument('-L','--lock',dest='lock',nargs='?',default=False,help="Lock the username.")
    parser.add_argument('-U','--unlock',dest='unlock',nargs='?',default=False,help="Ulock the username.")

    args = parser.parse_args()

    user = args.username
    pwd = args.pwd
    login_name = args.login_name
    group = args.group
    locked = args.lock
    unlock =args.unlock
        
    if args.admin:
#        print('admin is commite.')
        admin_add(user)
    if args.common and group:
#        print('group is commite.')
        com_add(user,group)
    if args.delete:
#        print('delete is commite.')
        user_del(user)   
    if login_name:
#        print('login_name is commite.')
        user_mod(user,pwd=None,login_name=login_name,group=None,lock=None,unlock=None)
    if group and  not args.common:
#        print('mode group is commite.')
        user_mod(user,pwd=None,login_name=None,group=group,lock=None,unlock=None)
    if locked:
        user_mod(user,pwd=None,login_name=None,group=None,lock=True,unlock=None)
    if unlock:
        user_mod(user,pwd=None,login_name=None,group=None,lock=None,unlock=True)
        
    
