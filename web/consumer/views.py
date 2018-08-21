from django.shortcuts import render

# Create your views here.

def consumer(request):
    return render(request,"consumer/user.html")

