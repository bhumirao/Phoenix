

from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.landing,name="first"),
    path("calneder",views.calendar,name="calendar"),
    path("login",views.login,name="login"),
]

