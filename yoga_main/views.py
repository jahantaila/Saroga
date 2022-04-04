from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
  return render(request, 'home.html')

def superpanel(request):
  return render(request, 'teachpanel.html')

def loginUser(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      print('user created')
      return redirect('superpanel')
    else:
      return redirect('home')
  else: 
    return render(request, 'login.html')

def signup(request):
  return render(request, 'signup.html')
  
def classes(request):
   return render(request, 'classes.html')

def resources(request):
   return render(request, 'resources.html')

def privacyPolicy(request):
   return render(request, 'privacypolicy.html')

def termsOfUse(request):
  return render(request, 'termsofuse.html')