from django.shortcuts import render
from .form import ShopUserRegisterForm, ShopUserLoginForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

# Create your views here.

def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST or None)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/account.html', content)

def register(request):
    title = 'register'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST)
        print('method POST')

        if register_form.is_valid():
            print('is valid')
            register_form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print(register_form.error_messages)
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))