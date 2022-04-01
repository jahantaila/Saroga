from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def superpanel(request):
  return render(request, 'superpanel.html')

def signUp(request):
  return render(request, 'signup.html')
