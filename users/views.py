from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.db import IntegrityError
from django.db.models import Q
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, logout
from users.forms import UserForm
from polls.models import Results


@login_required
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
        return redirect(reverse('user_base'))

    return redirect(reverse('user_base'))


def create_group(request):
    if request.method == "POST":
        group_name = request.POST.get('group_name')
        group = Group(name=group_name)
        group.save();

        return redirect(reverse('group_add'))
    else:
        groups = Group.objects.all()

    return render(request, 'user/add_group.html', {'groups': groups})

def add_permissions(request):
    perms = Permission.objects.all();
    content_type = ContentType.objects.get_for_model(User)

    print(content_type)

    return render(request, 'user/permissions.html', {'perms': perms})


@csrf_protect
def registration(request):
    form = None

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('user_base'))
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
def user_edit(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        user.groups.name = "cookie"
        user.groups.permissions = ['one', 'two']

        redirect(reverse('user_edit'))

    return render(request, 'user/edit.html', {'user_data': user})


def send_notification(request):
    subject = 'like a cat'
    message ='got milk?'
    from_email = 'cookie@epasts.lv'
    to_list = ['stabone@inbox.lv', 'ivars883@inbox.lv']

    # try:
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    # except SMTPException:
        # return HttpResponseRedirect('/')

    return redirect('/user/')


"""
    for future implementation
"""
@csrf_protect
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # redirect() redirect to a success page
        else:
            # return a 'disabled login' error message
            # redirect()
            pass
    else:
        # return an 'invalid login' error message
        pass


def find_user(request):
    if request.method == 'POST':
        search_str = request.POST.get('user')
        users = User.objects.filter(Q(username__contains=search_str) | Q(last_name__contains=search_str))

        return render(request, 'user/index.html', {'users': users})


def user_delete(request):
    if request.method == 'POST':
        user_id = request.POST.get('userID')
        user = User.objects.get(id=user_id)
        user.delete()

        return redirect(reverse('user_base'))
