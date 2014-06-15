from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    users = User.objects.all()
    return render(request, 'user/index.html', {'users': users})


def create(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
    else:
        email = ''
        password = ''

    try:
        user = User.objects.create_user(username='',password='')
        user.email = 'Jone@epasts.lv'
        user.first_name = 'Ivars'
        user.last_name = 'Naglis'

        user.save()
    except IntegrityError:
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/user/')


@csrf_protect
def registration(request):
    form = None

    if request.method == "POST":
        # user = User.objects.create_user(username=user_name,email=e_mail,password=password)
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')
    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {'form': form})


@login_required
@csrf_protect
def user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    return render(request, 'user/profile.html', {'user': user})


@login_required
@csrf_protect
def edit_profile(request):
    user_id = request.user.id
    # load user data
    # all goodies in form
    return render(request, 'user/profile.html', {'form': form})


def send_notification(request):
    subject = 'like a cat'
    message ='got milk?'
    from_email = 'cookie@epasts.lv'
    to_list = ['stabone@inbox.lv', 'ivars883@inbox.lv']

    # try:
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    # except SMTPException:
        # return HttpResponseRedirect('/')

    return HttpResponseRedirect('/user/')


"""
    for future implementation
"""
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
            pass
    else:
        # return an 'invalid login' error message
        pass

