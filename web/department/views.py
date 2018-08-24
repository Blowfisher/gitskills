from django.shortcuts import render
import sys
# Create your views here.

sys.path.append('./..')

from consumer.models import *

def department(request):
    users = Sa_user().show()
    data = Sa_group().show()
    return render(request,"department/department.html",{"data":data,"users":users})

def group_info(request):
    group = Sa_group().show()
    return HttpResponse(json.dumps({"group":group}),content_type="application/json")


def group_add(name,path,desc):
    b = Sa_group()
    s = b.creator(name,path,desc)    
    s.save()
    return

