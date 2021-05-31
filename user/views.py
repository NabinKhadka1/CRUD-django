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
