from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from messaging.models import Contacts, Messages
from messaging.forms import ContactForm, MessagingForm

# Create your views here.

@login_required
def add_message(request):
    if request.method == "POST":
        message = MessagingForm(request.POST)
    else:
        pass
    
    return render(request, 'message/index.html')

@login_required
def delete_message(request):
    if request.method == "POST":
        Messages.object.delete()
        
        return HttpResponceRedirect('/message/inbox/')

@login_required
def add_contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
    else:
        pass
    
    return render(request, 'tempalte')

@login_required
def delete_contact(request):
    if request.method == "POST":
        return HttpResponseRedirect('/contact/list/')
