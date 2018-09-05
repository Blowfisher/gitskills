from django.shortcuts import render
import os,sys,logging

# Create your views here.

logger = logging.getLogger('django')

def browse(request):
    return render(request,"browse/view.html")
