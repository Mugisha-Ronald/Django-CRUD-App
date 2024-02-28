from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Soldier,Address

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username','email','password1','password2']


class CreateSoldierForm(forms.ModelForm):
    class Meta:
        model = Soldier

        fields = ['army_no','rank','full_names','dateOfBirth','formal_educ','courses_attnd','appointment','status']



class AddHomeForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('district','county','sub_county','parish','vilage','soldier')

        