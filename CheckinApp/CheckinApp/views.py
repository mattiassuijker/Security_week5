from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('home')
	return render(request, 'home.html') 

def login(request):
    # return HttpResponse('login')
	return render(request, 'login.html') 