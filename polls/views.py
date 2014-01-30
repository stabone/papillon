from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# my imports
from polls.models import Poll, Choise
from polls.forms  import PollForm, ChoiseForm


# Create your views here.
def index(request, page_numb):
    poll_list = Poll.objects.all()
    paginator = Paginator(poll_list, 2)
    
    try:
        poll_slice = paginator(page_numb)
    except PageNotAnInteger:
        poll_slice = paginator.page(1)
    except EmptyPage:
        poll_slice = paginator.page(paginator.num_pages)

    return render(request, 'poll/index.html', {'data': poll_slice})


@csrf_protect
def add_poll(request):
    if(request.method == "POST"):
        form = PollForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        form = PollForm()

    return render(request, 'poll/add.html', {'form': form})


@csrf_protect
def add_choise(request, poll_id):
    if(request.method == "POST"):
        form = ChoiseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        data = Poll.objects.get(id=poll_id)
        choise = Choise(poll_id=data)
        form = ChoiseForm(instance=choise)

    return render(request, 'poll/add_choise.html', {'form': form})


@csrf_protect
def edit_poll(request, poll_id):
    record = Poll.objects.get(id=poll_id)
    if(request.method == "POST"):
        form = PollForm(request.POST, instance=record)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        data = Poll.objects.get(id=poll_id)
        form = PollForm(instance=data)

    return render(request, 'poll/edit_poll.html', {'form': form})

@csrf_protect
def edit_choise(request, choise_id):
    if(request.method == "POST"):
        form = ChoiseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        data = Choise.objects.get(id=choise_id)
        form = ChoiseForm(instance=data)

    return render(request, 'poll/edit_choise.html', {'form': form})


def take_poll(request, poll_id):
    data = Choise.objects.filter(poll_id=poll_id)

    return render(request, 'poll/take.html', {'data': data})


def delete_poll(request, poll_id):
    record = Poll.objects.get(id=poll_id)
    if(record.delete()):
        return HttpResponseRedirect('/poll/')

    return HttpResponseRedirect('/poll/')


def delete_choise(request, choise_id):
    record = Choise.objects.get(id=choise_id)
    if(record.delete()):
        return HttpResponseRedirect('/poll/')

    return HttpResponseRedirect('/poll/')
