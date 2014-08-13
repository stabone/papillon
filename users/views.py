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


@login_required
def list_groups(request):
    groups = Group.objects.all()

    return render(request, 'user/group.html', {'groups': groups})


@login_required
@csrf_protect
def create_group(request):
    if request.method == "POST":
        group_name = request.POST.get('group_name')

        group = Group(name=group_name)
        group.save();

        return redirect(reverse('group_list'))
    else:
        groups = Group.objects.all()

    return render(request, 'user/add_group.html', {'groups': groups})


@login_required
@csrf_protect
def add_group(request):
    if request.method == "POST":
        group_id = request.POST.get('group_id')

        group = get_object_or_404(Group, id=group_id)
        request.user.groups.add(group)

    return redirect(reverse('group_create'))


@login_required
def edit_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    return render(request, 'user/edit_group.html', {'group': group})


@login_required
@csrf_protect
def update_group(request):
    if request.method == "POST":
        group_id = request.POST.get('group_id')
        group_name = request.POST.get('group_name')

        group = get_object_or_404(Group, id=group_id)
        group.name = group_name

        group.save()

    return redirect(reverse('group_list'))


@login_required
@csrf_protect
def delete_group(request):
    if request.method == "POST":
        group_id = request.POST.get('group_id')

        group = get_object_or_404(Group, id=group_id)
        group.delete()

    return redirect(reverse('group_list'))


def add_group_perms(request,group_id=None):
    if request.method == "POST":
        group_id = request.POST.get('group_id')
        perms_list = request.POST.getlist('permissions')
        try:
            pk_list = [int(perm_id) for perm_id in perms_list]
        except ValueError:
            print('cant convert value')

        group = get_object_or_404(Group, id=group_id)
        perms = Permission.objects.in_bulk(pk_list)

        print(perms.count)

        group.permissions = perms
        group.save()

        return redirect(reverse('group_perms_add'))

    else:
        groups = Group.objects.all()
        perms = Permission.objects.all()

    return render(request, 'user/permissions.html', {'perms': perms, 'groups': groups})


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

    return render(request, 'user/registration.html', {'form': form})


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

