from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
  return render(request, 'home.html')

def superpanel(request):
  return render(request, 'teachpanel.html')

def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('teachpanel')
    else:
      return redirect('home')
  else: 
    return render(request, 'login.html')

def signup(request):
  form = UserCreationForm()
  context = {'form': form}
  return render(request, 'signup.html', context)
  
def classes(request):
   return render(request, 'classes.html')

def resources(request):
   return render(request, 'resources.html')