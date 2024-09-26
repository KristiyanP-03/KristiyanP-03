from django.urls import path

from DjangoProject.App.views import *

urlpatterns = [
    path("", home),
    path("profile/create/", profile_creation, name="")
]