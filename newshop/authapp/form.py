from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import ShopUser

from django.contrib.auth.forms import UserChangeForm


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        # print(self.fields)
        # self.fields['first_name'].verbose_name.attrs.update({'class':'text-info'})
        # self.fields['first_name'].widget.attrs.update({'class': 'text-info'})
        # for field in self.fields.values():
        #     print(field.verbose_name)
            # field.widget.attrs.update({'class':'text-info'})
        # self.fields['first_name'].verbose_name = 'first name'
        # self.fields['last_name'].verbose_name = 'last name'
        self.fields['username'].label = 'nickname'
        self.fields['email'].label = 'email'
        # self.fields['password1'].verbose_name = 'password'
        self.fields['password2'].label = 're-enter password'
        for field in self.fields.values():
            field.help_text = ''

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
