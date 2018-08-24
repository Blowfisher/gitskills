
#!/usr/bin/env python
#coding:utf8

import os,sys
import logging
from subprocess import Popen,PIPE
import confhandler
import dirhandler
import userhandler

"""
root_path = None
departmente_ment[]
user_add=[]

mode_change

conf_set
start smb
"""
mode = 770

"""install samba server."""
yum cean all && yum update && yum -y install samba


dirhandler.Dcreater(rootpath)
os.chmod(rootpath,mode)

dirtmp = os.path.join(rootpath,tmppath)
dirhandler.Dtmp(dirtmp)

"""list []"""
for i in admin_user_list:
    userhandler.admin_add(i)
    dirpath = os.path.join(rootpath,i)
    dirhandler.Dcreater(dirpath)
    dirhandler.Down(dirpath,i,i)
    os.chmod(dirpath,mode)

"""dict in list [{},{}]"""
for i in com_user_list:
    userhandler.com_add(i[0],i[1])
#    dirpath = os.path.join(os.path.join(rootpath,i[0]),i[1])
#    dirhandler.Dcreater(dirpath)    
#    dirhandler.Down(dirpath,i[0])
    os.chmod(dirpath,mode)


"""add smb user"""
"""echo -e "%s\n%s"|smbpasswd -s -a %s"""%(a1,a1,b1)

    
"""{global:[{},{}]}"""

def smb_set(smb_confname,args*):
    














