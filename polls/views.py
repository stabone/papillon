from django.shortcuts import render
from django.http import HttpResponseRedirect

# my code
from polls.models import Poll
from polls.forms  import PollForm


# Create your views here.
def index(request):
    data = Poll.objects.all()
    return render(request, 'poll/index.html', {'data': data})

def add(request):
    if(request.method == "POST"):
        form = PollForm(request.POST)
        if( form.is_valid() ):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        form = PollForm()

    return render(request, 'poll/add.html', {'form': form})
def edit_poll(request, poll_id):
    record = Poll.objects.filter(poll_id)

