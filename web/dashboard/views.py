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
from wsamba import wsuser

wconf = confhandler.Config_helper(confhandler.wsamba_conf)
conf = wconf.config_key_get('WSAMBA','samba_conf')
logger = logging.getLogger('django')


def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def guider(request):
    return render(request,"dashboard/user_guider.html")

def conf_export(request):
    filer = requesti.FILES.get('file','')
    with open(filer.name,'wb+') as f:
        for chunk in f.chunks():
            f.write(chunk)
    try:
        sconf = confhandler.Config_helper(filer.name)
        for section in sconf.sections():
            for option in sconf.items(section):
                if option == 'comment':
                    userhandler.dpt_add(section)
                    Sa_dpt().creator(section,option,sconf.get(section,option)).save() 
                    Sa_deploy().creator(section,option[0],option[1]).save()
                else:
                    Sa_deploy().creator(section,option[0],option[1]).save()
        os.path.remove(filer.name)
        os.path.remove(conf)
        with open(conf,'wb+') as f:
            sconf.write(f)
    except Exception as e:
        print(e)
    return JsonResponse({'success':True})


