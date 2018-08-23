from django.shortcuts import render
from models import *
import sys
# Create your views here.

sys.path.append('./..')

from consumer.models import *


def deploy(request):
    data = Sa_deploy().show()
    tmp =set()
    for i in data:
        tmp.add(i["section_name"])
    tmp = list(tmp)
    return render(request,"deploy/setting.html",{"section":tmp,"deploy":data})


def deploy_add(section_name,key_name,value_name):
    dpment = Sa_group().show()
    if section_name not in  [i.groupname for i in dpment]:
        return False
    b = Sa_deploy()
    s = b.creator(section_name,key_name,value_name)
    s.save()
    return 

