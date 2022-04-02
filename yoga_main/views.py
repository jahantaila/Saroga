from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
  return render(request, 'home.html')

def superpanel(request):
  return render(request, 'superpanel.html')

def login(request):
  return render(request, 'login.html')

def signup(request):
  form = UserCreationForm()
  context = {'form': form}
  return render(request, 'signup.html', context)
