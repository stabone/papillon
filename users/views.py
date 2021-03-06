#-*- coding: utf-8 -*-
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import Http404, HttpResponse
from django.db import IntegrityError
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.models import CustomUser
from users.forms import UserForm, UserInfoForm


@login_required
def index(request):
    users = CustomUser.objects.all()
    return render(request, 'user/index.html', {'users': users})


@login_required
def user_profile(request):
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)

    return render(request, 'user/profile.html', {'user': user})


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

        return redirect(reverse_lazy('group_list'))
    else:
        groups = Group.objects.all()

    return render(request, 'user/add_group.html', {'groups': groups})


@login_required
@csrf_protect
def add_group(request):
    if request.method == "POST":
        group_id = request.POST.get('group_id', '')

        group = get_object_or_404(Group, id=group_id)
        request.user.groups.add(group)

    return redirect(reverse_lazy('group_create'))


@login_required
def edit_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    return render(request, 'user/edit_group.html', {'group': group})


@login_required
@csrf_protect
def update_group(request):
    if request.method == "POST":
        group_id = request.POST.get('group_id', '')
        group_name = request.POST.get('group_name', '')

        group = get_object_or_404(Group, id=group_id)
        group.name = group_name

        group.save()

    return redirect(reverse_lazy('group_list'))


@login_required
@csrf_protect
def delete_group(request):
    if request.method == "POST":
        group_id = request.POST.get('group_id', '')

        group = get_object_or_404(Group, id=group_id)
        group.delete()

    return redirect(reverse_lazy('group_list'))


@login_required
@csrf_protect
def add_group_perms(request,group_id=None):
    if request.method == "POST":
        try:
            group_id = request.POST.get('group_id', '')
            perms_list = request.POST.getlist('permissions', '')
        except KeyError:
            raise Http404

        try:
            pk_list = [int(perm_id) for perm_id in perms_list]
        except ValueError:
            print('cant convert value')
            raise Http404

        group = get_object_or_404(Group, id=group_id)
        perms = Permission.objects.in_bulk(pk_list)

        print(perms.count)

        group.permissions = perms
        group.save()

        return redirect(reverse_lazy('group_perms_add'))

    else:
        groups = Group.objects.all()
        perms = Permission.objects.all()

    return render(request, 'user/permissions.html', {'perms': perms, 'groups': groups})


@csrf_protect
def registration(request):
    form = None

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('user_profile'))
    else:
        form = UserForm()

    return render(request, 'user/registration.html', {'form': form})

@login_required
def user_form(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    user_form = UserInfoForm(instance=user)

    return render(request, 'user/edit.html', {'form': user_form})


@login_required
@csrf_protect
def user_edit(request):

    if request.method == 'GET':
        return redirect(reverse_lazy('user_profile'))

    if request.method == 'POST':
        print(request.POST)
        user = get_object_or_404(CustomUser, id=request.user.id)
        user_form = UserInfoForm(request.POST, instance=user)

        user_form.save()

        return redirect(reverse_lazy('user_profile'))
        # return render(request, 'user/edit.html', {'form': user_form})


"""
    for future implementation
"""
@csrf_protect
def login_user(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            pass
    else:
        pass


@login_required
@csrf_protect
def find_user(request):

    if request.method == 'POST':
        try:
            search_str = request.POST.get('user', '')
        except KeyError:
            raise Http404

        users = CustomUser.objects.filter(
                Q(user_name__contains=search_str) |
                Q(last_name__contains=search_str))

        return render(request, 'user/index.html', {'users': users})


@login_required
@csrf_protect
def user_delete(request):

    if request.method == 'GET':
        return redirect(reverse_lazy('user_base'))

    user_list = request.POST.getlist('data', [])
    print(user_list)

    for user_id in user_list:
        custom_user = get_object_or_404(CustomUser, id=user_id)
        custom_user.delete()

    return redirect(reverse_lazy('user_base'))


@login_required
def user_block(request):
    response_data ={}

    if request.method == 'GET':
        response_data['error'] = 'Nederīgs pieprasījums'
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    user_list = json.loads(data)

    for user_obj in user_list:
        user_id = user_obj['id']
        user_status = user_obj['status']
        custom_user = get_object_or_404(CustomUser, id=user_id)
        custom_user.is_active = True if user_status == 1 else False
        custom_user.save()

    response_data['ok'] = 'Informācija atjaunota'

    return HttpResponse(json.dumps(response_data), content_type='application/json')


def instructor_list(request):
    authors = CustomUser.objects.filter(user_type=2)

    return render(request, 'instructors/instructors.html', {'authors': authors})


def create_admin(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    user.is_admin = True
    user.user_type = 3

    user.save()

    return redirect(reverse_lazy('user_profile'))


def create_author(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    user.user_type = 2

    user.save()

    return redirect(reverse_lazy('user_profile'))

