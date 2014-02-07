from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

# my imports
from polls.models import Polls, Questions, Choises
from polls.forms  import PollForm, QuestionForm, ChoiseForm


# Create your views here.
def index(request, page_numb=None):
    poll_list = Polls.objects.all()
    paginator = Paginator(poll_list, 2)

    try:
        poll_slice = paginator.page(page_numb)
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
def add_question(request, poll_id):
    if(request.method == "POST"):
        form = QuestionForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        try:
            data = Polls.objects.get(id=poll_id)
        except ObjectDoesNotExist:
            pass

        question = Questions(poll_id=data)
        form = QuestionForm(instance=question)

    return render(request, 'poll/add.html', {'form': form})


@csrf_protect
def add_choise(request, question_id, poll_id):
    if(request.method == "POST"):
        form = ChoiseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        try:
            # data = Polls.objects.get(id=poll_id)
            data = Questions.objects.filter(poll_id=poll_id)
        except ObjectDoesNotExist:
            pass

        # choise = Choises(poll_id=data)
        # choise = Choises(question_id=data)
        # form = ChoiseForm(instance=choise)
        form = ChoiseForm()

    return render(request, 'poll/add_choise.html', {'form': form})


@csrf_protect
def edit_poll(request, poll_id):
    try:
        record = Polls.objects.get(id=poll_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/poll/')

    if(request.method == "POST"):
        form = PollForm(request.POST, instance=record)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        data = Polls.objects.get(id=poll_id)
        form = PollForm(instance=data)

    return render(request, 'poll/edit_poll.html', {'form': form})


@csrf_protect
def edit_question(request, question_id):
    try:
        data = Questions.objects.get(id=question_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/poll/')

    if(request.method == "POST"):
        form = QuestionForm(request.POST, instance=data)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        form = QuestionForm(instance=data)

    return render(request, 'poll/edit_question.html', {'form': form})


@csrf_protect
def edit_choise(request, choise_id):
    if(request.method == "POST"):
        form = ChoiseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        try:
            data = Choises.objects.get(id=choise_id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/poll/')

        form = ChoiseForm(instance=data)

    return render(request, 'poll/edit_choise.html', {'form': form})


def take_poll(request, poll_id):
    try:
        data = Choises.objects.filter(poll_id=poll_id)
    except ObjectDoesNotExist:
        pass

    return render(request, 'poll/take.html', {'data': data})

def take_question(request, poll_id):
    try:
        data = Questions.objects.filter(poll_id=poll_id)
    except ObjectDoesNotExist:
        pass

    return render(request, 'poll/take.html', {'data': data})

# here should be right check
def delete_poll(request, poll_id):
    try:
        record = Polls.objects.get(id=poll_id)
    except ObjectDoesNotExist:
        pass

    if(record.delete()):
        return HttpResponseRedirect('/poll/')

    return HttpResponseRedirect('/poll/')


def delete_question(request, question_id):
    try:
        record = Questions.objects.get(id=question_id)
    except ObjectDoesNotExist:
        pass

    if(record.delete()):
        return HttpResponseRedirect('/poll/')

    return HttpResponseRedirect('/poll/')


def delete_choise(request, choise_id):
    try:
        record = Choises.objects.get(id=choise_id)
    except ObjectDoesNotExist:
        pass

    if(record.delete()):
        return HttpResponseRedirect('/poll/')

    return HttpResponseRedirect('/poll/')
