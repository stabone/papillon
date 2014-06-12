from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from messaging.models import Contacts, Messages
from messaging.forms import ContactForm, MessagingForm


@login_required
def inbox(request):
    messages = Messages.objects.all() # for todo filter() by user
    return render(request, 'message/inbox.html', {'messages': messages})


@login_required
def add_message(request):
    if request.method == "POST":
        message = MessagingForm(request.POST)
        if message.is_valid():
            message.save()
            return HttpResponseRedirect('/message/')
    else:
        message = MessagingForm()

    return render(request, 'message/send.html', {'form': message})


@login_required
def read_message(request,msg_id):
    message = Messages.objects.get(id=msg_id)

    return render(request, 'message/read.html', {'message': message})


@login_required
def delete_message(request):
    if request.method == "POST":
        Messages.object.delete()

        return HttpResponseRedirect('/message/inbox/')


@login_required
def add_contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
    else:
        contact = ContactForm()

    return render(request, 'contacts/add.html', {'form': contact})


@login_required
def delete_contact(request):
    if request.method == "POST":
        return HttpResponseRedirect('/contact/list/')
