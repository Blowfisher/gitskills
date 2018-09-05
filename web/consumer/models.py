from django.db import models
from django.db.models import Manager

# Create your models here.


class Sa_user(models.Model):
    username = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    userpwd = models.CharField(max_length=255)
    user_locked =models.BooleanField(default=False)
    stat = models.BooleanField(default=True)
    login_ip = models.CharField(max_length=32)
    last_login = models.DateTimeField(auto_now=True)
    user_role = models.IntegerField(default='3')
    class Meta():
        db_table = 'sa_user'
    @classmethod
    def creator(cls,name,pwd,role="",desc="",login_ip=""):
        b = Sa_user()
        b.username = name
        b.userpwd = pwd
        b.desc = desc
        b.user_role = role
        b.login_ip = login_ip
        return b
    def show(self):
        b = Sa_user.objects.values()
        return b

class Sa_dpt(models.Model):
    dptname = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    stat = models.BooleanField(default=True)
    creator_time = models.DateTimeField(auto_now=True)
    dpt_locked = models.BooleanField(default=False)
    class Meta():
        db_table = 'sa_dpt'
 
    @classmethod
    def creator(cls,name,desc):
        b = Sa_dpt()
        b.dptname = name
        b.desc = desc
        return b
    def show(self):
        b = Sa_dpt.objects.values()
        return b
   

class Sa_role(models.Model):
    role_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255)
    stat = models.BooleanField(default=True)
    class Meta():
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
