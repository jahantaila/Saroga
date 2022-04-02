from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def superpanel(request):
  return render(request, 'teachpanel.html')

def login(request):
  return render(request, 'login.html')

def classes(request):
  return render(request, 'classes.html')