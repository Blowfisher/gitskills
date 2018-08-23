from django.db import models
from django.db.models import Manager

# Create your models here.


class Sa_user(models.Model):
    username = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    userpwd = models.CharField(max_length=255)
    user_locked =models.BooleanField(default=False)
    stat = models.BooleanField(default=True)
    login_ip = models.CharField(max_length=32)
    last_login = models.DateTimeField(auto_now=True)
    user_group = models.ForeignKey('Sa_group')
    role_id = models.ForeignKey('Sa_role')
    class Medata():
        db_table = 'sa_user'
    @classmethod
    def creator(cls,name,pwd,group,role,desc=None,login_ip=None):
        b = Sa_user()
        b.username = name
        b.userpwd = pwd
        b.desc = desc
        b.user_group = group
        b.role_id = role
        b.login_ip = login_ip
        return b
    def show(self):
        b = Sa_user.objects.values()
        return b

class Sa_group(models.Model):
    groupname = models.CharField(max_length=20)
    groupath = models.CharField(max_length=32)
    desc = models.CharField(max_length=255)
    state = models.BooleanField(default=True)
    creator_time = models.DateTimeField(auto_now=True)
    group_locked = models.BooleanField(default=False)
    class Medata():
        db_table = 'sa_group'
 
    @classmethod
    def creator(cls,name,path,desc=None):
        b = Sa_group()
        b.groupname = name
        b.groupath = path
        b.desc = desc
        return b
    def show(self):
        b = Sa_group.objects.values()
        return b
   
'''
class Sa_root(models.Model):
    root_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255,blank=True)
    creator_time = models.DateTimeField(auto_now=True)
    stat = models.BooleanField(default=True)
    class Medata():
        db_table = 'sa_root'
    
    @classmethod
    def creator(cls,name,desc=None):
        b = Sa_root()
        b.root_name = name
        b.desc = desc
        return b
'''

class Sa_role(models.Model):
    role_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    stat = models.BooleanField(default=True)
    class Medata():
        db_table = 'sa_role'

    @classmethod
    def creator(cls,name,desc):
        b = Sa_role()
        b.role_name = name
        b.desc = desc
        return b
    def show(self):
        b = Sa_role.objects.values()
        return b
