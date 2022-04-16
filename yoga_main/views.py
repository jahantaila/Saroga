from cmath import log
from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def home(request):
  return render(request, 'home.html')

@login_required(login_url = ('/login/'))
def dashboard(request):
  return render(request, 'teachpanel.html')

def registerUser(request):
  return render(request, 'register.html')


def nextScreen(request):
  return render(request, 'nextscreen.html')


def loginUser(request):
  if request.user.is_authenticated:
    return redirect('dashboard')
  else:
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('dashboard')
      else:
        return redirect('login')
    else: 
      return render(request, 'login.html')

def logoutUser(request):
  logout(request)
  return redirect('home')

def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        newuser = User.objects.create_user(username, email, password)
        newuser.first_name = firstname
        newuser.last_name = lastname

        newuser.save()

        return redirect(request, 'loginUser')
    return render(request, 'signup.html')
  
def classes(request):
   return render(request, 'classes.html')

def resources(request):
   return render(request, 'resources.html')

def privacyPolicy(request):
   return render(request, 'privacypolicy.html')

def termsOfUse(request):
  return render(request, 'termsofuse.html')
