from django.shortcuts import render #, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrig.auth import authenticate, login, logout


# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'user/index.html', {'users': users})


def create(request):
    try:
        user = User.objects.create_user(username='jone', password='cookie')
        # user.username = 'Cookie'
        # user.password = 'cookie'
        user.email = 'Jone@epasts.lv'
        user.first_name = 'Ivars'
        user.last_name = 'Naglis'

        user.save()
    except IntegrityError:
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/user/')


@csrf_protect
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')
    else: # GET and another animals
        form = UserCreationForm()

    return render(request, 'user/register.html', {'form': form})


@login_required
@csrf_protect
def edit_profile(request, user_id):
    # load user data
    # all goodies in form
    return render(request, 'user/profile.html', {'form': form})


@csrf_protect
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # redirect to a success page
        else:
            # return a 'disabled login' error message
    else:
        # return an 'invalid login' error message


@login_required
@csrf_protect
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/course/')

