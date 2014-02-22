from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

# my imports
from polls.models import Polls, Questions, Choises, Results
from polls.forms  import PollForm, QuestionForm, ChoiseForm


# Create your views here.
def index(request, page_numb=None):
    poll_list = Polls.objects.all()
    paginator = Paginator(poll_list, 5)

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

    return render(request, 'poll/add_poll.html', {'form': form})


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

    return render(request, 'poll/add_question.html', {'form': form})


@csrf_protect
def add_choise(request, question_id, poll_id):
    if(request.method == "POST"):
        form = ChoiseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/take/{0}/question/'.format(poll_id))
    else:
        try:
            data = Questions.objects.get(id=question_id)
        except ObjectDoesNotExist:
            pass

        choise = Choises(question_id=data)
        form = ChoiseForm(instance=choise)

    return render(request, 'poll/add_choise.html', {'form': form, 'poll': data.poll_id})


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
    try:
        data = Choises.objects.get(id=choise_id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/poll/')

    if(request.method == "POST"):
        form = ChoiseForm(request.POST, instance=data)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/poll/')
    else:
        form = ChoiseForm(instance=data)

    return render(request, 'poll/edit_choise.html', {'form': form})


def take_poll(request, poll_id):
    try:
        data = Choises.objects.filter(poll_id=poll_id)
    except ObjectDoesNotExist:
        pass

    return render(request, 'poll/take.html', {'data': data})


def packQuestions(choises):
    # magic of television
    """
        ansers are stored in dictionary where as key
        is used answer pk

        returns list with ansers dictionaries
    """
    answer_list = []
    for answer in choises:
        answer_list.append((answer.id, answer.option,))

    return answer_list


def take_question(request, poll_id):
    try:
        data = Questions.objects.filter(poll_id=poll_id)
        answer_list = []
        for rec in data:
            choises = Choises.objects.filter(question_id=rec.id)
            """
                answer list is appendet to anser stack
                for all questions
            """
            question_list = packQuestions(choises)
            answer_list.append((rec.id, question_list,))
    except ObjectDoesNotExist:
        pass

    return render(request, 'poll/take.html', {'data': data, 'answers': answer_list})


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


@csrf_protect
def save_poll_results(request):
    if request.method == "POST":
        # QueryDict converting to python dictionary
        post_dict = request.POST.dict()
        #poll = Polls.objects.get(id=1)
        obj_list = []

        for key, value in post_dict.iteritems():
            please_int = key[-1]
            try:
                questiond = int(please_int,base=10)
                obj_list.append(Results(poll_id=1,question_id=questiond,answer_id=value))
            except ValueError:
                print("Cound't convert '{0}' to integer".format(please_int))

        if obj_list:
            all_results = Results.objects.bulk_create(obj_list)

    return HttpResponseRedirect('/poll/')

