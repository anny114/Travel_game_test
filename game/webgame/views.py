from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserInfoForm
# Create your views here.

def index(request):
    return render(request, 'index.html', {
    })

def userinfo(request):    
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserInfoForm()
    return render(request, 'userinfo.html', {'form': form})

def success(request):
    return render(request, 'success.html')
