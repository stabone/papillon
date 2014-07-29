from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse


from polls.models import Polls, Questions, Choises, Results
from polls.forms  import PollForm, QuestionForm, ChoiseForm


def create_poll_dict(poll_list):
    poll_dict = {}

    for record in poll_list:
        poll_dict[record.id] = {
            'id': record.id,
            'poll': record.poll,
            'description': record.description
        }

    return poll_dict


def pop_done_polls(poll_list,user_obj):
    poll_dict = create_poll_dict(poll_list)
    done_polls = Results.objects.filter(user=user_obj)
    valid_polls = []

    for record in done_polls:
        if record.poll in poll_dict:
            del poll_dict[record.poll]

    for key in poll_dict:
        valid_polls.append(poll_dict[key])

    return valid_polls


# Create your views here.
def index(request,page_numb=None):
    poll_list = Polls.objects.all()
    poll_dict = pop_done_polls(poll_list,request.user)

    paginator = Paginator(poll_dict, 5)

    try:
        poll_slice = paginator.page(page_numb)
    except PageNotAnInteger:
        poll_slice = paginator.page(1)
    except EmptyPage:
        poll_slice = paginator.page(paginator.num_pages)

    return render(request, 'poll/index.html', {'data': poll_slice})


@login_required
@csrf_protect
def add_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST, request.user)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.user = request.user
            poll.save()
            return redirect('/poll/')
    else:
        form = PollForm()

    return render(request, 'poll/poll_form.html', {'form': form})


@login_required
@csrf_protect
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            poll = get_object_or_404(Polls, id=request.POST.get('poll'))

            all_form = form.save(commit=False)
            all_form.poll = poll
            all_form.save()
            return redirect(reverse('take_poll',args=[poll.id]))
    else:
        form = QuestionForm()

    return render(request, 'poll/question_form.html', {'form': form})


@login_required
@csrf_protect
def add_choise(request,poll_id,question_id):
    if request.method == "POST":
        form = ChoiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('edit_poll_content',args=[poll_id]))
    else:
        data = get_object_or_404(Questions,id=question_id)
        choise = Choises(question=data)
        form = ChoiseForm(instance=choise)

    return render(request, 'poll/choise_form.html', {'form': form, 'poll': data.poll})


@login_required
@csrf_protect
def edit_poll(request,poll_id):
    record = get_object_or_404(Polls,id=poll_id)

    if request.method == "POST":
        form = PollForm(request.POST,instance=record)
        if(form.is_valid()):
            form.save()
            return redirect('/poll/')
    else:
        form = PollForm(instance=record)

    return render(request, 'poll/poll_form.html', {'form': form})


@login_required
@csrf_protect
def edit_question(request,question_id):
    data = get_object_or_404(Questions,id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST,instance=data)
        if(form.is_valid()):
            form.save()
            return redirect('/poll/')
    else:
        form = QuestionForm(instance=data)

    return render(request, 'poll/question_form.html', {'form': form})


@login_required
@csrf_protect
def edit_choise(request,poll_id,choise_id):
    data = get_object_or_404(Choises,id=choise_id)

    if request.method == "POST":
        form = ChoiseForm(request.POST,instance=data)
        if(form.is_valid()):
            form.save()
            return redirect(reverse('edit_poll_content',args=[poll_id]))
    else:
        form = ChoiseForm(instance=data)

    return render(request, 'poll/choise_form.html', {'form': form})


def get_choise_list(choise_obj):
    choise_list = []
    for choise in choise_obj:
        choise_list.append({'id': choise.id, 'option': choise.option, 'correct': choise.correct})

    return choise_list


def parse_question(question_obj):
    question_list = []
    for question in question_obj:
        choises = Choises.objects.filter(question=question)
        question_list.append({
            'id': question.id,
            'question': question.question,
            'choises': get_choise_list(choises)
        })

    return question_list


@login_required
@csrf_protect
def edit_poll_content(request,poll_id):
    poll = Polls.objects.get(id=poll_id)

    if request.method == "POST":
        form = QuestionForm(request.POST, poll)
        if(form.is_valid()):
            form.save()
            return redirect(reverse('take_poll',args=[poll.id]))
    else:
        questions = Questions.objects.filter(poll=poll)
        data = parse_question(questions)

        form = QuestionForm()

    return render(request, 'poll/edit_poll_content.html', {'form': form, 'questions': data, 'poll': poll})

@login_required
def take_poll(request, poll_id):
    poll = Polls.objects.get(id=poll_id)
    questions = Questions.objects.filter(poll=poll)
    poll_data = {'id': poll.id, 'name': poll.poll}
    data = parse_question(questions)

    return render(request, 'poll/take_poll.html', {'poll': poll_data, 'questions': data})


# here should be right check
@login_required
@csrf_protect
def delete_poll(request):

    if request.method == "POST":
        poll_id = request.POST.get('pollID')
        record = get_object_or_404(Polls,id=poll_id)
        record.delete()
        return redirect('/poll/')

    return redirect('/poll/')


@login_required
@csrf_protect
def delete_question(request):

    if request.method == "POST":
        question_id = request.POST.get('questionID')
        record = get_object_or_404(Questions,id=question_id)
        poll_id = record.poll.id
        record.delete()
        return redirect(reverse('take_poll',args=[poll_id]))

    return redirect('/poll/')


@login_required
@csrf_protect
def delete_choise(request):

    if request.method == "POST":
        choise_id = request.POST.get('choiseID')
        poll_id = request.POST.get('pollID')
        record = get_object_or_404(Choises,id=choise_id)

        record.delete()
        return redirect(reverse('edit_poll_content',args=[poll_id]))

    return redirect('/poll/')


@login_required
@csrf_protect
def save_poll_results(request):
    if request.method == "POST":
        """ QueryDict converting to python dictionary """
        post_dict = request.POST.dict()
        obj_list = []

        for key, value in post_dict.iteritems():
            please_int = key[-1]
            try:
                questiond = int(please_int,base=10)
                obj_list.append(Results(user=request.user,poll=1,question=questiond,answer=value))
            except ValueError:
                print("Cound't convert '{0}' to integer".format(please_int))
                # return HttpResponseRedirect('404')

        if obj_list:
            """ bulk create will perfor save """
            all_results = Results.objects.bulk_create(obj_list)

    return redirect('/poll/')


def get_user_statistic(request):
    data = Results.objects.filter(user=request.user)
    return render(request, 'poll/statistic.html', {'data': data})
