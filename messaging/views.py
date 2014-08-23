from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from messaging.models import Contacts, Messages
from messaging.forms import ContactForm, MessagingForm


@login_required
def inbox(request, page_numb=None):
    message_list = Messages.objects.filter(trash=False).order_by('-sent_at') # by user

    paginator = Paginator(message_list, 25)

    try:
        message_slice = paginator.page(page_numb)
    except PageNotAnInteger:
        message_slice = paginator.page(1)
    except EmptyPage:
        message_slice = paginator.page(paginator.num_pages)

    return render(request, 'message/messages.html', {'messages': message_slice})


@login_required
@csrf_protect
def add_message(request):
    if request.method == "POST":
        message = MessagingForm(request.POST)

        if message.is_valid():
            rec = message.save(commit=False)
            rec.user_from = request.user
            rec.save()

            return redirect(reverse('messaging_inbox'))
    else:
        message = MessagingForm()

    return render(request, 'message/send.html', {'form': message})


@login_required
def read_message(request, msg_id):
    message = Messages.objects.get(id=msg_id)

    return render(request, 'message/read.html', {'message': message})


@login_required
def respond_message(request, msg_id):
    if request.method == 'GET':
        responce = get_object_or_404(Messages,id=msg_id)
        message = Messages(user_to=responce.user_from,title=responce.title)
        form = MessagingForm(instance=message)

    return render(request, 'message/respond.html', {'form': form})


@login_required
@csrf_protect
def restore_message(request):
    if request.method == 'POST':
        message_id = request.POST.get('messageID')

        message = Messages.objects.get(id=message_id)
        message.trash = False
        message.save()

        return redirect(reverse('messaging_inbox'))

    return redirect(reverse('messaging_trash'))


@login_required
def trash_message(request, page_numb=None):
    """
    Trash message list
    """
    message_list = Messages.objects.filter(trash=True)

    paginator = Paginator(message_list, 25)

    try:
        message_slice = paginator.page(page_numb)
    except PageNotAnInteger:
        message_slice = paginator.page(1)
    except EmptyPage:
        message_slice = paginator.page(paginator.num_pages)

    return render(request, 'message/messages.html', {'messages': message_slice})


@login_required
@csrf_protect
def to_trash_message(request):
    """
    Message moving to trash
    """
    if request.method == "POST":
        messageID = request.POST.get('messageID')

        message = get_object_or_404(Messages, id=messageID)

        message.trash = True
        message.save()

    return redirect(reverse('messaging_inbox'))


@login_required
@csrf_protect
def delete_message(request):
    if request.method == "POST":
        messageID = request.POST.get('messageID')
        message = get_object_or_404(Messages, id=messageID)
        message.delete()

    return redirect(reverse('messaging_inbox'))


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
