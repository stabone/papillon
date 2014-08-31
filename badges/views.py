#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from badges.forms import BadgeForm, BadgeTypeForm
from badges.models import Badges, BadgeTypes


def get_badges(request):
    badge = Badges.objects.fiter(user=request.user)
    return render(request, 'badges/badges.html', {'badges': badges})


@login_required
@csrf_protect
def add_badge(request):
    if request.method == 'POST':
        badge = BadgeForm(request.POST)
        badge.save()

    return redirect()


@login_required
@csrf_protect
def edit_badge(request, badge_id):
    badge = get_object_or_404(Badges, id=badge_id)

    return render(request, '', {})


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

