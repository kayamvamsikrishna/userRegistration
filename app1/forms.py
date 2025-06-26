from django import forms
from app1.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        #fields='__all__'
        exclude=['user']




'''
If we are sending parent tables form object and
child tables fOrm object into same HTML page,.... 
then we should not represent parent tables column in 
input elements
'''