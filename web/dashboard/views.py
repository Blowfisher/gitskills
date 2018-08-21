from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def guider(request):
    return render(request,"dashboard/user_guider.html")
