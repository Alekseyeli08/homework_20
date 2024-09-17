from catalog.forms import StyleFormMixin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from users.models import User
from django import forms

class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone' , 'country')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()