from django import forms
from .models import Adultmodel,contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Adultmodel
        fields = ['image', 'name', 'gender','size','gener','date','memo']


#class Signupform(UserCreationForm):
#    email = forms.EmailField(max_length=254, help_text='emailアドレスは必須です')

#    class Meta:
#        model = User
#        fields = [
#            'username',
#            'email',
#            'password1',
#            'password2',
#        ]
class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields=['title','message','email']