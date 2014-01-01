from django.shortcuts import render
from django.http import HttpResponseRedirect

# my code
from polls.models import Poll, Choise
from polls.forms  import PollForm, ChoiseForm


# Create your views here.
def index(request):
    data = Poll.objects.all()
    return render(request, 'poll/index.html', {'data': data})


def add_poll(request):
    if(request.method == "POST"):
        form = PollForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        form = PollForm()

    return render(request, 'poll/add.html', {'form': form})


def add_choise(request, poll_id):
    if(request.method == "POST"):
        form = ChoiseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        form = ChoiseForm()

    return render(request, 'poll/add_choise.html', {'form': form})


def edit_poll(request, poll_id):
    record = Poll.objects.get(id=poll_id)
    if(request.method == "POST"):
        form = PollForm(request.POST, instance=record)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    elif(request.method == "GET"):
        record = Poll.objects.get(id=poll_id)
        form = CategorieForm(instance=data)

    return render(request, 'course/edit_poll.html', {'form': form})


def take_poll(request, poll_id):
    data = Choise.objects.filter(poll_id=poll_id)
    return render(request, 'poll/take.html', {'data': data})


