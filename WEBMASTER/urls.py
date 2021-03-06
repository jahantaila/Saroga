"""WEBMASTER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from yoga_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('classes/', views.classes, name='classes'),
    path('privacypolicy/', views.privacyPolicy, name='privacyPolicy'),
    path('termsofuse/', views.termsOfUse, name='termsOfUse'),
    path('resources/', views.resources, name='resources'), 
    path('logout/', views.logoutUser, name='logout'),
    path('createclass/', views.create_class, name='create_class'),
    path('about/', views.about, name='about'),
    path('references/', views.references, name='references'),

]