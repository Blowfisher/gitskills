#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
import sys
import json
import base64
import logging

import wsamba
from wsamba import wsuser
from wsamba import userhandler
from department.models import *

logger = logging.getLogger('django')

# Create your views here.

def consumer(request):
    role = Sa_role().show()
    user = Sa_user().show()
    dpment = Dpt_user().show()
    if request.is_ajax():
        return JsonResponse(json.dumps({"users":user,"dpment":dpment,"role":role}))
    else:
        return render(request,"consumer/user.html",{"users":user,"dpment":dpment,"role":role})


def add_user(request):
    name = request.POST.get('username','')
    pwd = request.POST.get('pwd','')
    role = request.POST.get('role','')
    desc = request.POST.get('desc','')
    if Sa_user.objects.filter(username=name):
        return JsonResponse({"success":False,"msg":"用户已存在!"})
    b = Sa_user()
    b.creator(name,pwd,role,desc).save()
    logger.info('USER '+name+'was add to db.')

    userhandler.admin_add(name)

    wuser = wsuser.wsuser(name,pwd)
    wuser.wuadd()

    user = Sa_user().show()
    for i in user:
        if name == i["username"]:
            uid = i["id"]
    return JsonResponse(json.dumps({"success":True}))

def user_edit(request):
    name = request.POST.get('uname','')
    uid = request.POST.get('uid','')
    role = request.POST.get('role','')
    desc = request.POST.get('desc','')

    userid = Sa_user.objects.get(id=uid)
    logger.info(userid.userpwd + "-------------------")
    pwd = userid.userpwd
    if userid.username != name:
        userhandler.user_del(userid.username)
        userhandler.admin_add(name)
        userid.username = name
        wsuser.wsuser(name).wudel()
        wsuser.wsuser(name).wuadd(name,pwd)
        wsuser.wsuser(name,lock=True).wuenable()
    else:
        wsuser.wsuser(name,pwd).wuadd()
        wsuser.wsuser(name,unlock=True).wuenable()
    Sa_user.objects.filter(id=uid).update(username=name,desc=desc,userpwd=pwd,user_role=role)
    return JsonResponse(json.dumps({"uname":name,"uid":uid,"role":role,"desc":desc,"success":True}))    

def reset_pwd(request):
    name = request.POST.get('uname','')
    pwd = request.POST.get('pwd','')
    uid = request.POST.get('uid','')
    wsuser.wsuser(name).wudel()
    wsuser.wsuser(name,pwd).wuadd()
    wsuser.wsuser(name,unlock=True).wuenable()
    Sa_user.objects.filter(id=uid).update(userpwd=pwd)
    return JsonResponse(json.dumps({"success":True}))    
    


def user_lock(request):
    name = request.POST.get('uname','')
    uid = request.POST.get('uid','')
    lock = int(request.POST.get('lock',''))

    userid = Sa_user.objects.filter(id=uid)
    if lock:
        wsuser.wsuser(name,lock=True).wupause()
        userid.update(stat = False)
        userid.update(user_locked = True)
    else:
        wsuser.wsuser(name,unlock=True).wuenable()
        userid.update(stat = True)
        userid.update(user_locked = False)
    return JsonResponse(json.dumps({"success":True}))    

def user_delete(request):
    uid = request.POST.get('uid',' ')
    logger.info("----------------------")
    logger.info(uid)
    userid = Sa_user.objects.get(id=uid)
    Dpt_user.objects.filter(username=userid.username).delete()
    userhandler.user_del(userid.username)
    wsuser.wsuser(userid.username).wudel()
    Sa_user.objects.filter(username=userid.username).delete()
    return JsonResponse({"success":True,"msg":"已删除."})

