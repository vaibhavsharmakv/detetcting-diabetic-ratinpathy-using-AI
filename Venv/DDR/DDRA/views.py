from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseForbidden

from .models import eye_images as ei
from .forms import eye_images_form
from DDR.settings import BASE_DIR

from django.core.files.storage import FileSystemStorage

from subprocess import run, PIPE 
import sys,os,uuid





def display_eye(request):
   
    var = {
        'obj' :''# scrpt.stdout,
    }
    return render(request,"home.html",var)



# Create your views here.
def home_view(request, *args, **kwargs):
    var = {}
    if request.method == "POST":
        form = eye_images_form(request.POST,request.FILES)
        if form.is_valid():
            new_form = form.save() 
            print(new_form.id)
        return redirect('/display/')

    else:
        form = eye_images_form()
        var = {
                'form' : form,
            }
    
    return render(request, "home.html", var)

