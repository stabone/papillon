from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse

from djang.forms import BadgeForm, BadgeTypeForm
from djang.models import Badges, BadgeTypes


def get_badges(request):
    badge = Badges.objects.fiter(user=request.user)
    return render(request, 'badges/badges.html', {'badges': badges})


@login_required
def add_badge(request):
    if request.method == 'POST':
	badge = BadgeForm(request.POST)
	badge.save()

    return redirect()


@login_required
def edit_badge(request, badge_id):
    badge = get_object_or_404(Badges, id=badge_id)

    return render(request, '', {})


@login_required
def delete_badge(request, badge_id):
     
    badge = get_object_or_404(Badges, id=badge_id)
    badge.delete()

    return render(request, '', {})


@login_required
def add_badge_type(request):
    return render(request, '', {})


@login_required
def edit_badge_type(request):
    
    form = 
    return render(request, '', {})


@login_required
def delete_badge_type(request, type_id):
 
    badge = get_object_or_404(BadgeTypes, id=type_id)
    badge.delete()

    return render(request, '', {})

