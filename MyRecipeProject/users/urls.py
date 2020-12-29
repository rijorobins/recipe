"""MyRecipeProject URL Configuration

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
from users.views import UserRegistration,user_login,user_home,ProfileCreate,view_profile,edit_profile,user_logout
urlpatterns = [
    path("registration",UserRegistration.as_view(),name="registration"),
    path("login",user_login.as_view(),name="login"),
    path("home",user_home.as_view(),name="home"),
    path("create",ProfileCreate.as_view(),name="profilecreate"),
    path("view",view_profile.as_view(),name="view"),
    path("edit",edit_profile.as_view(),name="edit"),
    path("logout",user_logout.as_view(),name="logout")

]
