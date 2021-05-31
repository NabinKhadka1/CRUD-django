from user.models import Registration
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm
from .models import Registration

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    data = Registration.objects.all()
    return render(request,'index.html',{'form':form,'data':data})

def update(request,id):
    if request.method == 'POST':
        reg = Registration.objects.get(pk=id)
        form = RegistrationForm(request.POST,instance=reg) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        reg = Registration.objects.get(pk=id)
        form = RegistrationForm(instance=reg)    
    return render(request,'update.html',{'form':form})

def delete(request,id):
    if request.method == 'POST':
        dat = Registration.objects.get(pk=id)
        dat.delete()
        return HttpResponseRedirect('/')
