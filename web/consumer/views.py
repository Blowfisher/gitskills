from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
import sys
import json

sys.path.append('./..')
from wsamba import *


# Create your views here.

def consumer(request):
    role = Sa_role().show()
    group = Sa_group().show()
    user = Sa_user().show()
    if request.is_ajax():
        return JsonResponse(json.dumps({"user":user}))
    else:
        return render(request,"consumer/user.html",{"users":user,"group":group,"role":role})


def user_add(request):
    userhandler.admin_add
