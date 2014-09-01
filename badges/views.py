#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from badges.forms import BadgeForm, BadgeTypeForm
from badges.models import Badges, BadgeTypes


def get_badges(request):
    badges = Badges.objects.fiter(user=request.user)
    return render(request, 'badges/badges.html', {'badges': badges})


@login_required
@csrf_protect
def add_badge(request):
    if request.method == 'POST':
        badge = BadgeForm(request.POST)
        badge.save()

    return redirect(reverse('badge_base'))


@login_required
@csrf_protect
def edit_badge(request, rec_id):
    try:
        badge_id = int(rec_id)
    except ValueError:
        # izmests 404
        pass

    badge = get_object_or_404(Badges, id=badge_id)
    form = BadgeForm(instance=badge)

    return render(request, '', {'form': form})


@login_required
@csrf_protect
def update_badge(request):
    if request.method == 'POST':

        badge = get_object_or_404(Badges, id=request.POST.get('badge_id'))

        form = BadgeForm(request.POST, instance=badge)

        if form.is_valid():
            form.save()

            return redirect(reverse('badge_base'))

    return redirect(reverse('badge_base'))


@login_required
@csrf_protect
def delete_badge(request, badge_id):

    badge = get_object_or_404(Badges, id=badge_id)
    badge.delete()

    return render(request, '', {})


@login_required
@csrf_protect
def add_badge_type(request):

    form = BadgeTypeForm()

    return render(request, '', {'form': form})


@login_required
@csrf_protect
def edit_badge_type(request):

    form = BadgeTypeForm()

    return render(request, '', {'form': form})


@login_required
@csrf_protect
def delete_badge_type(request, type_id):

    badge = get_object_or_404(BadgeTypes, id=type_id)
    badge.delete()

    return render(request, '', {})

