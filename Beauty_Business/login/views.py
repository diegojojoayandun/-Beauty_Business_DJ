from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from management import templates
from django.contrib import messages


def signup(request):
    """Register a new user in the database"""
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
                messages.error(
                    request, "El usuario ya se encuentra registrado"
                    )
                return render(
                    request, "signup.html", {
                        'form': UserCreationForm,
                        })
        messages.error(request, "Contraseña no coincide")
        return render(
            request, "signup.html", {
                'form': UserCreationForm})


def signout(request):
    """Logout an user from the app and delete the current session"""
    logout(request)
    return redirect("signin")


def signin(request):
    """Login an user in the database"""
    if request.method == 'GET':
        return render(request, "signin.html", {'form': AuthenticationForm})
    else:
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])

        if user is None:
            messages.error(request, "nombre de usuario o password incorrectos")
            return render(
                request, 'signin.html', {
                    'form': AuthenticationForm})
        else:
            login(request, user)
            print(user.username)
            return redirect('/management/', user.username)
