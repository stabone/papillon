from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return redirect(reverse('article_base'))


def handler400(request):
    return render(request, 'helper/400_handler.html', {})


def handler403(request):
    return render(request, 'helper/403_handler.html', {})


def handler404(request):
    return render(request, 'helper/404_handler.html', {})


def handler500(request):
    return render(request, 'helper/500_handler.html', {})

