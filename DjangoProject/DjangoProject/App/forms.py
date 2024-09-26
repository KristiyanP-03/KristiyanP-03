from django import forms

from DjangoProject.App.models import Profile



class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ['first_name', 'last_name',
                  'month', 'day', 'year', 'gender',
                  'email',
                  'username', 'password', 'confirm_password']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',

            'month': 'Month',
            'day': 'Day',
            'year': 'Year',
            'gender': 'Gender',

            'email': 'Email',

            'username': 'Username',
            'password': 'Password',
            'confirm_password': 'Confirm Password',

        }

class ExtendedProfileForm(ProfileCreationForm):
    pass


class ContentUploadingForm(forms.ModelForm):
    pass

class ExtendedContentUploadingForm(ContentUploadingForm):
    pass