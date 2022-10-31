

from django.contrib import admin
from django.urls import path
from home import views
from home.models import postEnquiry 


urlpatterns = [
    path("",views.landing,name="first"),
    path("calneder",views.calendar,name="calendar"),
    path("login",views.login,name="login"),
    path("logv",views.forum,name="forum"),
    
]

