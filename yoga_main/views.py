from datetime import datetime
from pyexpat.errors import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from yoga_main.models import UserDetails, YogaClass
from django.contrib import messages
from django.http import HttpResponseRedirect

import jwt
import requests 
import json
from time import time




# Enter your API key and your API secret
API_KEY = 'AHt18e6vT5CZu33gAmWfMQ'
API_SEC = 'I6D8Y85GN1IplXu7V0SIg4I6AlGYRfuXnlo7'

# create a function to generate a token
# using the pyjwt library


def generateToken():
	token = jwt.encode(

		# Create a payload of the token containing
		# API Key & expiration time
		{'iss': API_KEY, 'exp': time() + 5000},

		# Secret used to generate token signature
		API_SEC,

		# Specify the hashing alg
		algorithm='HS256'
	)
	return token

# create json data for post requests
meetingdetails = {"topic": "The title of your zoom meeting",
				"type": 2,
				"start_time": "2022-04-17T10: 00:00",
				"duration": "45",
				"timezone": "America/New_York",
				"agenda": "test",

				"recurrence": {"type": 1,
								"repeat_interval": 1
								},
				"settings": {"host_video": "true",
							"participant_video": "true",
							"join_before_host": "False",
							"mute_upon_entry": "False",
							"watermark": "true",
							"audio": "voip",
							"auto_recording": "cloud"
							}
				}

# send a request with headers including
# a token and meeting details


def createMeeting():
  headers = {'authorization': 'Bearer ' + generateToken(), 'content-type': 'application/json'}
  r = requests.post(
  f'https://api.zoom.us/v2/users/me/meetings', headers=headers, data=json.dumps(meetingdetails))
  y = json.loads(r.text)
  join_URL = y['join_url']
  meetingPassword = y['password']
  return join_URL, meetingPassword



# run the create meeting function
createMeeting()

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
		return redirect('/dashboard/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(username=username, password=password)
      
			if user is not None:
				login(request, user)
				return redirect('/dashboard')
			else:
        
				messages.error(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

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
    date = datetime.today().strftime('%m-%d-%y') 
    time = datetime.now().strftime("%I:%M %p")
    link, password = createMeeting()
    YogaClass.objects.create(name=name, user=user, tag = tag, description=description, rating=rating, date=date, time = time, link = link, password = password)
    return redirect('dashboard')
  return render(request, 'createclass.html')

def resources(request):
   return render(request, 'resources.html')

def privacyPolicy(request):
   return render(request, 'privacypolicy.html')

def termsOfUse(request):
  return render(request, 'termsofuse.html')

def about(request):
  return render(request, 'about.html')

def references(request):
  return render(request, 'references.html')
