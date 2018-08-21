from django.shortcuts import render

# Create your views here.

def deploy(request):
    return render(request,"deploy/setting.html")

