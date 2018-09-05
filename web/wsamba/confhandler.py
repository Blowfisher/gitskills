#!/usr/bin/env python
#coding:utf8

import os
import sys
from  ConfigParser import ConfigParser
import subprocess
import logging


wsamba =os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"data")
wsamba_conf = os.path.join(wsamba,"conf/wsamba.conf")
wsamba_log= os.path.join(wsamba,"log/wsamba.log")
logger = logging.getLogger('django')



class Config_helper(ConfigParser):
    def __init__(self,smb_config):
        self.smb_conf = smb_config
        self.config = ConfigParser(allow_no_value=True)
        self.config.read(self.smb_conf)
    def config_save(self):
        with open(self.smb_conf,'wb+') as f:
            self.config.write(f) 
        logger.info('CONFIGFILE: '+self.smb_conf+' was saved.')

    def config_set(self,args):
        """
	args is a list nest structor
        in a little list. need have 3 parameter. is seciton option value
	"""
        data = args
        try:
            for i in data: 
                self.sname = i[0]
                self.kname = i[1]
                self.vname = i[2]
                self.config.set(self.sname,self.kname,self.vname)
            logger.info('Kname: '+self.kname+' was set.')
            return 
        except Exception as e:
            logger.error(e)
            return 1

    def config_key_get(self,sname,kname):
        self.sname = sname
        self.kname = kname   
        try:
            data = self.config.get(self.sname,self.kname)
            logger.info('Kname: '+self.kname+' was get.')
            return data
        except Exception as e:
            logger.error(e)
            return 1

        

    def Section_get(self,sname):
        """ data is list contain some tuple.
            tupel[0] is a key, tuple[1] is a value."""
        self.sname = sname 
        try:
            data = self.config.items(self.sname)
            logger.info('Department :'+self.sname+' was show.')
            return data
        except Exception as e:
            logger.error(e)
            return 1

    def Create_section(self,sname):
        self.sname = sname
        try:
            self.config.add_section(self.sname)
            logger.info('Department :'+self.sname+' was added.')
            return
        except Exception as e:
            logger.error(e)
            return 1

    def Remove_section(self,sname):
        self.sname = sname
        try:
            self.config.remove_section(self.sname)
            logger.warn('Department :'+self.sname+' was removed.')
            return
        except Exception as e:
            logger.error(e)
            return 1

    def Remove_key(self,sname,kname):
        self.sname = sname
        self.kname = kname
        try:
            self.config.remove_option(self.sname,self.kname)
            logger.warn('Keyname:'+self.kname+' was removed.')
            return
        except Exception as e:
            logger.error(e)
            return 1



if __name__ == '__main__':
    print('Good!')   
