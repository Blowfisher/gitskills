from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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
    sconf = confhandler.Config_helper(conf)

    b = Sa_deploy()
    b.creator(section,key,value).save()
    sconf.set(section,key,value)
    sconf.config_save()
    return JsonResponse({'section':section,'key':key,'value':value})

def deploy_del(request):
    value = request.POST.get('value','')
    section = request.POST.get('section','')
    key = request.POST.get('key','')
    sconf = confhandler.Config_helper(conf)
    
    b = Sa_deploy.objects.get(key_name=key,section_name=section)
    b.delete()
    sconf.Remove_key(section,key)
    sconf.config_save()
    return JsonResponse({'delete':True})




def deploy_edit(request):
    section = request.POST.get('section','')
    key = request.POST.get('key','')
    value = request.POST.get('value''')
    sconf = confhandler.Config_helper(conf)

    try:
        b = Sa_deploy.objects.get(key_name=key,section_name=section)
        b.section_name = section
        b.key_name = key
        b.value_name = value
        b.save()
    except Exception as e:
        b = Sa_deploy()
        b.creator(section,key,value).save()
    
    sconf.config_set([section,key,value])
    sconf.config_save()
    return JsonResponse({'change':True})


