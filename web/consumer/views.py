from django.shortcuts import render
from django.http import HttpResponse
from models import *

# Create your views here.

def consumer(request):
    user = Sa_user().show()
    return render(request,"consumer/user.html",{"users":user})



def user_info(request):
    if is_ajax():
        user = Sa_user().show()
        return HttpResponse(json.dumps({"user":user}),content_type="application/json")
    else:
        return render(request,"consumer/user.html") 


    
def role_add(name,desc):
    b = Sa_role()
    s = b.creator(name,desc)
    s.save()
    return

def user_add(name,pwd,group,role,desc="",login_ip=""):
    b = Sa_user()
    s = b.creator(name,pwd,group,role,desc="",login_ip="")
    s.save()
    return

