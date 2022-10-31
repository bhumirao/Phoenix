

from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.landing,name="first"),
    #path("home",views.home,name="home")
]
