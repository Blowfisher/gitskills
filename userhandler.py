#!/usr/bin/env python
#coding:utf8

import os,sys
import logging
from subprocess import Popen,PIPE
import argparse




    
def admin_add(username):
    acmd = """useradd -M -s /sbin/nologin %s"""%username
    adata = Popen(acmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = adata.stderr.read()
    if error:
        print(error)
    return

def com_add(username,group):
    ccmd = """useradd -M -s /sbin/nologin -G %s %s"""%(group,username)
    cdata = Popen(ccmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = cdata.stderr.read()
    if error:
        print(error)
    return

def user_del(username):
    dcmd = """userdel -r %s"""%username
    ddata = Popen(dcmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = ddata.stderr.read()
    if error:
        print(error)
    return

def user_mod(username,pwd=None,login_name=None,group=None,lock=None,unlock=None):
    def cpwd(username,pwd):
        pcmd = """usermod -p %s %s"""%(pwd,username)
        pdata = Popen(pcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = pdata.stderr.read()
        if error:
            print(error)
        return 

    def cname(username,login_name):
        cncmd = """usermod -l %s %s"""%(login_name,username)
        cndata = Popen(cncmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = cndata.stderr.read()
        if error:
            print(error)
        return 

    def cgroup(username,group):
        cgcmd = """usermod -g %s %s"""%(group,username)
        cgdata = Popen(cgcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = cgdata.stderr.read()
        if error:
            print(error)
        print(cgdata.stdout.read())
        return 
   
    def locker(username):
        lcmd = """usermod -L %s"""%username
        ldata = Popen(lcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = ldata.stderr.read()
        if error:
            print(error)
        return 
   
    def ulocker(username):
        ulcmd = """usermod -U %s"""%username
        uldata = Popen(ulcmd,stdout=PIPE,stderr=PIPE,shell=True)
        error = uldata.stderr.read()
        if error:
            print(error)
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
        
    
