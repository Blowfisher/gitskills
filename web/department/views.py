from django.shortcuts import render
import sys
# Create your views here.

sys.path.append('./..')

from consumer.models import *

def department(request):
    data = Sa_group.objects.all()
    return render(request,"department/department.html",{"data":data})

def group_info(request):
    group = Sa_group().show()
    return HttpResponse(json.dumps({"group":group}),content_type="application/json")


def group_add(name,path,desc):
    b = Sa_group()
    s = b.creator(name,path,desc)    
    s.save()
    return

