from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from management import templates



def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html", {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/management/')
            except IntegrityError:
                return render(
                    request, "signup.html", {
                        'form': UserCreationForm,
                        'error': 'Usuario ya existe'})

        return render(
            request, "signup.html", {
                'form': UserCreationForm, 'error': 'Password No corresponde'})


def signout(request):
    logout(request)
    return redirect("signin")


def signin(request):
    if request.method == 'GET':
        return render(request, "signin.html", {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])

        if user is None:
            return render(
                request, 'signin.html', {
                    'form': AuthenticationForm,
                    'error': 'nombre de usuario o password incorrectos'})
        else:
            login(request, user)
            print(user.username)
            return redirect('/management/',user.username)


