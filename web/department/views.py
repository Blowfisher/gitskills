#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import sys
import json
import logging


from department.models import *
from deploy.models import *
from consumer.models import *
import wsamba
from wsamba import confhandler
from wsamba import userhandler

wconf = confhandler.Config_helper(confhandler.wsamba_conf)
conf = wconf.config_key_get('WSAMBA','samba_conf')
logger = logging.getLogger('django')


def department(request):
    users = Dpt_user().show()
    data = Sa_dpt().show()
    if request.is_ajax():
        return JsonResponse(json.dumps({"data":data,"users":users}))
    else:
        return render(request,"department/department.html",{"data":data,"users":users})
        


def dpt_add(request):
    dpt_name = request.POST.get('dptname','')
#    path = request.POST.get('path','')
    desc = request.POST.get('desc','')

    b = Sa_dpt()
    b.creator(dptname,desc).save()    
    
    b = Sa_deploy()
    b.creator(dptname,"comment",desc).save()
    b.creator(dptname,"valid users","@"+dptname).save()
    
    sconf = confhandler.Config_helper(conf)
    sconf.Create_section(dptname)
    sconf.config_set([[dptname,'comment',desc],[dptname,"valid users","@"+dptname]])
    sconf.config_save()

    userhandler.dpt_add(name)
    bb = Sa_dpt.objects.get(dptname=dpt_name)
    return JsonResponse(json.dumps({"did":bb.id,"dptname":dpt_name,"desc":desc,"stat":True}))

def dpt_user(request):
    gid = request.POST.get('gid','')
    usernames = request.POST.getlist('username')
    dpt_name = request.POST.get('dptname','')

    b = Dpt_user()
    dpt_user = Dpt_user().show()
    for i in usernames:
        for j in dpt_user:
            if j["username"] == i and j["Dpt_name"] == dptname:
                continue
            else:
                b.creator(username,userdesc,dpt).save()
    for i in dpt_user:
        if i["dptname"] == dptname:
            if i["username"] not in usernames:
                name_notin = Dpt_user.objects.filter(username=i["username"],dptname=i["dptname"]) 
                name_notin.delete() 
    for i in usernames:
        user_dpt = Dpt_user.objects.filter(username = i)
        group = []
        for j in user_dpt:
            group.append(j["dptname"])
        userhandler.cgroup(i,group)
    return 

def dpt_edit(request):
    gid = request.POST.get('gid','')
    dpt_name = request.POST.get('dptname','')
    desc = request.POST.get('desc','')
    b = Sa_dpt.objects.get(id=gid)
    
    if dpt_name != b.dptname:
        sconf = confighandler.Config_helper(conf)
        sa_dpt = Sa_dpt.objects.get(id=gid)       
        dpt_user = Dpt_user.objects.filter(dptname=sa_dpt.dptname)
        deploy_name = Sa_deploy.objects.filter(section_name=sa_dpt.dptname)
        deploy_desc = Sa_deploy.objects.get(section_name=sa_dpt.dptname,key_name='comment')
        deploy_valid= Sa_deploy.objects.get(section_name=sa_dpt.dptname,key_name='valid users')

        userhandler.dpt_del(sa_dpt.dptname)
        sconf.remove_section(sa_dpt.dptname)
        sconf.add_section(dpt_name)
        deploy_name.update(section_name=dpt_name)
        deploy_desc.value_name = desc
        deploy_valid.value_name = '@'+dpt_name
        dpt_user.update(dptname=dpt_name)
        
        sa_dpt.dptname = dpt_name
        sa_dpt.desc = desc
        sa_dpt.save()
        
        dpt_deploy = Sa_deploy.objects.filter(section_name=dpt_name)
        for i in dpt_deploy:
            if i["is_delete"] is False:
                if i["key_name"] == "comment":
                    sconf.set(i['section_name'],i['key_name'],desc)
                else:
                    sconf.set(i['section_name'],i['key_name'],i['value_name'])
        sconf.config_save()  
        userhandler.dpt_add(dpt_name)
    else:
        sconf = confighandler.Config_helper(conf)
        sa_dpt = Sa_dpt.objects.get(id=gid)       
        sa_deploy = Sa_deploy.objects.get(section_name=sa_dpt.dptname,key_name=sa_dpt.desc)
        
        sa_deploy.value_name = desc
        sa_deploy.save()
        sa_dpt.desc = desc
        sa_dpt.save()
    
        sconf.set(dpt_name,'comment',desc)
        sconf.config_save()
    return 

def dpt_del(request):
    gid = request.POST.get('gid','')
    dpt_name = request.POST.get('dptname','')
    sconf = confighandler.Config_helper(conf)
    sa_dpt = Sa_dpt.objects.get(id=gid)
    sa_deploy = Sa_deploy.objects.filter(section_name=dpt_name)
    dpt_user = Dpt_user.objects.filter(dptname=dpt_name)
    userhandler.dpt_del(dpt_name)
    
    sconf.remove_section(dpt_name)
    sa_dpt.delete()
    sa_deploy.delete()
    dpt_user.delete()
    return

def dpt_lock(request):
    gid = request.POST.get('pid','')
    dpt_name = request.POST.get('dptname','')
    dpt_locked = request.POST.get('dpt_locked','')
    if lock:
        sa_dpt = Sa_dpt.objects.get(id=gid)      
        sa_dpt.stat = False
        sa_dpt.dpt_lock = True
        sa_dpt.save()
        userhandler.dpt_del(dpt_name)
    else:
        sa_dpt = Sa_dpt.objects.get(id=gid)      
        sa_dpt.stat = True
        sa_dpt.dpt_lock = False
        sa_dpt.save()
        userhandler.dpt_add(dpt_name)
    return 
