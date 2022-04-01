from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')

def teachpanel(request):
  return render(request, 'teachpanel.html')