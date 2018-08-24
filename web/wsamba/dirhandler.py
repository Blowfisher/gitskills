#!/usr/bin/env python
#coding:utf8

import sys,os
import logging
import argparse


"""此模块需要完整路径 """



def Dcreater(pathame):
    dirtmp = os.path.sep 
    if os.path.exists(pathname):
	print('exists.')
    else:
	data = pathname.split(os.path.sep)
	for i in data[1:]:
	    dirtmp = os.path.join(dirtmp,i)
	    if os.path.exists(dirtmp):
		continue
	    else:
		try:
		    os.makedirs(dirtmp)
		except Exception as e:
		    return e

def Dcreaters(args):
    """各路径需要写绝对路径"""
    dir_list = args
    for i in dir_list:
	Dhandler(i)

def Dlooker(pathname):
    tmp = []
    for root,dirs,files in os.walk(pathname):
	tmp.append(dirs)
	tmp.append(files)
	print tmp
        yield tmp
	return 



def Down(pathname,username,groupname):
    ocmd = """chown %s:%s %s"""%(username,groupname,pathname)
    odata = Popen(ocmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = odata.stderr.read()
    if error:
        print(error)

def Dtmp(pathname):
    tcmd = """chmod ugo+rwtx %s"""%pathname
    tdata = Popen(tcmd,stdout=PIPE,stderr=PIPE,shell=True)
    error = tdata.stderr.read()
    if error:
        print(error)




if __name__ == '__main__':
    pathname = sys.argv[1]
    Dlookor(pathname)
