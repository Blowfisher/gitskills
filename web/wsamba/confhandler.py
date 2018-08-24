#!/usr/bin/env python
#coding:utf8

import os
import sys
from  ConfigParser import ConfigParser
import subprocess
import logging

from etc import conf

smb_conf = conf.smb_conf



class Config_helper(ConfigParser):
    def __init__(self,smb_config):
        self.smb_conf = smb_config
        self.config = ConfigParser(allow_no_value=True)
        
    
    def config_set(self,args):
        """
	args is a list nest structor
        in a little list. need have 3 parameter. is seciton option value
	"""
        self._temp_list = args
        try:
            with open(smb_conf,'wb') as f:
                for i in self._temp_list: 
                    self.sname = i[0]
                    self.kname = i[1]
                    self.vname = i[2]
                    self.config.set(self.sname,self.kname,self.vname)
                self.config.write(f)
            return 
        except Exception as e:
            return 1

    def config_key_get(self,sname,kname):
        self.sname = sname
        self.kname = kname   
        try:
            with open(smb_conf,'rb') as f:
                data = self.config.get(self.sname,self.kname)
                return data
        except Exception as e:
            return 1

    def config_view(self):
        return open(self.smb_conf,'r')
        

    def Section_get(self,sname):
        """ data is list contain some tuple.
            tupel[0] is a key, tuple[1] is a value."""
        self.sname = sname 
        try:
            data = self.config.items(self.sname)
            return data
        except Exception as e:
            return 1

    def Create_section(self,sname):
        self.sname = sname
        try:
            self.config.add_section(self.sname)
            return
        except Exception as e:
            return 1

    def Remove_section(self,sname):
        self.sname = sname
        try:
            self.remove_section(self.sname)
            return
        except Exception as e:
            return 1

    def Remove_key(self,sname,kname):
        self.sname = sname
        self.kname = kname
        try:
            self.config.remove_option(self.sname,self.kname)
            return
        except Exception as e:
            return 1



if __name__ == '__main__':
    print('Good!')   
