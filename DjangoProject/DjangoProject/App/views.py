from django.shortcuts import render

from DjangoProject.App.forms import ProfileCreationForm


# Create your views here.
def home(request):
    context = {}
    return render(request, "home.html", context)

def profile_creation(request):
    context = {
        'profile_creation_form': ProfileCreationForm(),
    }

    return render(request, "create-profile.html" ,context)