from django.shortcuts import render
from models import *
import sys
import logging

# Create your views here.


from consumer.models import *
from deploy.models import *
import wsamba
from wsamba import confhandler

wconf = confhandler.Config_helper(confhandler.wsamba_conf)
conf = wconf.config_key_get('WSAMBA','samba_conf')
logger = logging.getLogger('django')

def deploy(request):
    logger.info(request.path)
    data = Sa_deploy().show()
    tmp =set()
    for i in data:
        tmp.add(i["section_name"])
    tmp = list(tmp)
    return render(request,"deploy/setting.html",{"section":tmp,"deploy":data})


def deploy_add(request):
    section = request.POST.get("section","")
    key = request.POST.get("key","")
    value = request.POST.get("value","")
    sconf = confighandler.Config_helper(conf)

    b = Sa_deploy()
    b.creator(section,key,value).save()
    sconf.set(section,key,value)
    sconf.config_save()
    return JsonResponse(json.dumps({'section':section,'key':key,'value':value}))

def deploy_del(request):
    sid = request.POST.get('sid','')
    section = request.POST.get('section','')
    key = request.POST.get('key','')
    sconf = confighandler.Config_helper(conf)
    
    b = Sa_deploy.objects.get(id=sid)
    b.delete()
    sconf.Remove_key(section,key)
    sconf.config_save()
    return JsonResponse(json.dumps({'delete':True}))




def deploy_edit(request):
    sid = request.POST.get('sid','')
    section = request.POST.get('section','')
    key = request.POST.get('key','')
    value = request.POST.get('value''')
    sconf = confighandler.Config_helper(conf)

    b = Sa_deploy.objects.get(id=sid)
    b.section_name = section
    b.key_name = key
    b.value_name = value
    b.save()
    
    sconf.set(section,key,value)
    sconf.config_save()
    return JsonResponse(json.dumps({'change':True}))


