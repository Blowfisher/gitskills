from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
import sys
import json
import base64

'./..' in sys.path or sys.path.append('./..')
import wsamba
from wsamba import wsuer
from wsamba import userhandler
from department.models import *

# Create your views here.

def consumer(request):
    role = Sa_role().show()
    group = Sa_dpt().show()
    user = Sa_user().show()
    dpment = Dpt_user().show()
    if request.is_ajax():
        return JsonResponse(json.dumps({"user":user,"group":group,"dpment":dpment,"role":role}))
    else:
        return render(request,"consumer/user.html",{"users":user,"group":group,"dpment":dpment,"role":role})


def user_add(request):
    name = request.POST.get('uname','')
    pwd = request.POST.get('pwd','')
    group = request.POST.get('group','')
    role = request.POST.get('role','')
    desc = request.POST.get('desc','')

    b = Sa_user()
    b.creator(name,pwd,role,desc).save()

    userhandler.admin_add(name)

    wuser = wsuser.wsuser(name,pwd)
    wuser.wuadd()

    user = Sa_user().show()
    for i in user:
        if name == i["username"]:
            uid = i["id"]
    return JsonResponse(json.dumps({"uid":uid,"uname":name,"role":role,"desc":desc,"stat":True}))

def user_edit(request):
    name = request.POST.get('uname','')
    uid = request.POST.get('uid','')
    pwd = request.POST.get('pwd','')
    role = request.POST.get('role','')
    desc = request.POST.get('desc','')

    userid = Sa_user.objects.get(id=uid)

    if userid.username != name:
        userhandler.user_del(userid.username)
        userhandler.admin_add(name)
        userid.username = name
        wsuser.wsuser(name).wudel()
        wsuser.wsuser(name).wuadd(name,pwd)
        wsuser.wsuser(name,lock=True).wuenable()
    else:
        wsuser.wsuser(name).wuadd(name,pwd)
        wsuser.wsuser(name,unlock=True).wuenable()
    userid.username = name
    userid.desc = desc
    userid.userpwd = pwd 
    userid.user_role = role
    userid.save()
    return JsonResponse(json.dumps({"uname":name,"uid":uid,"role":role,"desc":desc,"stat":True}))    



def user_lock(request):
    name = request.POST.get('uname','')
    uid = request.POST.get('uid','')
    pwd = request.POST.get('pwd','')
    role = request.POST.get('role','')
    desc = request.POST.get('desc','')
    user_locked = request.POST.get('lock','')

    userid = Sa_user.objects.get(id=uid)
    if user_locked:
        wsuser.wsuser(name,lock=True).wupause()
        userid.stat = False
        userid.user_locked = True
        
    else:
        wsuser.wsuser(name,unlock=True).wuenable()
        userid.stat = True
        userid.user_locked = False
    return JsonResponse(json.dumps({"uname":name,"uid":uid,"role":role,"desc":desc,"stat":True}))    

def user_del(request):
    uid = request.GET.get('uid','')
    userid = Sa_user.objects.get(id=uid)
    userhandler.user_del(userid.username)
    wsuser.wsuser(userid.username).wudel()
    return True

