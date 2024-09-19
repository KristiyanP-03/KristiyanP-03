from django.urls import path

from DjangoProject.App.views import *

urlpatterns = [
    path("", home, home="home")
]