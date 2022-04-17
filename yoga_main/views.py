from datetime import datetime
from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from yoga_main.models import UserDetails, YogaClass
from django.contrib import messages

def home(request):
  return render(request, 'home.html')

@login_required(login_url = ('/login/'))
def dashboard(request):
  user = request.user 
  user_details = UserDetails.objects.get(username=user)  # or userdetails.objects.get(user=user)
  context = {
      "total_yoga_time": user_details.total_yoga_time,
      "sessions_joined": user_details.sessions_joined,
      "classes_num": YogaClass.objects.filter().count()

    }
  return render(request, 'dashboard.html', context, )

def registerUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        newuser = User.objects.create_user(username = username, email = email, password = password, 
          )
        newuser.save()
        
        user = authenticate(request, username=username, password=password)
        UserDetails.objects.create(   # creates a UserDetail object (another models.py model )          
                    username=username,
                    total_yoga_time = 0,
                    sessions_joined = 0,
                    skill_level = "beginner",
                    classes_created = 0,
                )
        if user is not None:
          login(request, user)
          return redirect('dashboard')
        else:
          return redirect('login')
    else:
      return render(request, 'register.html')


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
        messages.success(request, "Your Class has been successfully created" )
        return redirect('dashboard')

      else:
        return redirect('login')
    else: 
      return render(request, 'login.html')

def logoutUser(request):
  logout(request)
  return redirect('home')

@login_required(login_url = ('/login/'))
def classes(request):
   yoga_classes = YogaClass.objects.all()
   context = {
     'yoga_classes': yoga_classes
   }
   return render(request, 'classes.html', context)


@login_required(login_url = ('/login/'))
def create_class(request):
  if request.method == "POST":
    name = request.POST.get('name')
    user = request.user
    tag = request.POST.get('tag')
    description = request.POST.get('description')
    rating = 'No Ratings Yet'
    date = datetime.today().strftime('%Y-%m-%d')
    link = "http://meet.google.com/new"
    YogaClass.objects.create(name=name, user=user, tag = tag, description=description, rating=rating, date=date, link = link, )
    return redirect('dashboard')
  return render(request, 'createclass.html')


def resources(request):
   return render(request, 'resources.html')

def privacyPolicy(request):
   return render(request, 'privacypolicy.html')

def termsOfUse(request):
  return render(request, 'termsofuse.html')

