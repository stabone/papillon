from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from messaging.models import Contacts, Messages
from messaging.forms import ContactForm, MessagingForm


@login_required
def inbox(request):
    messages = Messages.objects.filter(trash=False) # by user
    return render(request, 'message/inbox.html', {'messages': messages})


@login_required
@csrf_protect
def add_message(request):
    if request.method == "POST":
        message = MessagingForm(request.POST)
        if message.is_valid():
            rec = message.save(commit=False)
            rec.user_from = request.user
            rec.save()
            return redirect('/message/')
    else:
        message = MessagingForm()

    return render(request, 'message/send.html', {'form': message})


@login_required
def read_message(request,msg_id):
    message = Messages.objects.get(id=msg_id)

    return render(request, 'message/read.html', {'message': message})


@login_required
def trash_message(request):
    messages = Messages.objects.filter(trash=True)

    return render(request, 'message/trash.html', {'messages': messages})


def to_trash_message(request):
    if request.method == "POST":
        messageID = request.POST.get('messageID')
        print(messageID)
        message = get_object_or_404(Messages, id=messageID)

        message.trash = True
        message.save()

        return redirect('/message/')

@login_required
def delete_message(request):
    if request.method == "POST":
        Messages.object.delete()

        return redirect('/message/inbox/')


@login_required
@csrf_protect
def add_contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
    else:
        contact = ContactForm()

    return render(request, 'contacts/add.html', {'form': contact})


@login_required
def delete_contact(request):
    if request.method == "POST":
        return redirect('/contact/list/')
