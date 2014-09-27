from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404


from polls.models import Polls, Questions, Choises, Results
from polls.forms  import PollForm, QuestionForm, ChoiseForm


# plain python functions
def get_latvian_date(date_obj):
    return date_obj.strftime('%Y.%M.%d %H:%m:%S')


def create_poll_dict(poll_list):
    poll_dict = {}

    for record in poll_list:
        poll_dict[record.id] = {
            'id': record.id,
            'poll': record.poll,
            'description': record.description,
            'created_at': get_latvian_date(record.created_at),
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
# plain python functions


@login_required
def index(request,page_numb=None):
    poll_list = Polls.objects.all()
    poll_dict = pop_done_polls(poll_list, request.user)

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
            return redirect(reverse('base_poll'))
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

            return redirect(reverse('take_poll', args=[poll.id]))
    else:
        form = QuestionForm()

    return render(request, 'poll/question_form.html', {'form': form})


@login_required
@csrf_protect
def add_question_for_poll(request, poll_id):

    poll = get_object_or_404(Polls, id=poll_id)

    form = QuestionForm()

    return render(request, 'poll/add_question.html', {'form': form, 'poll': poll})


@login_required
@csrf_protect
def add_choise(request, poll_id, question_id):
    if request.method == "POST":
        form = ChoiseForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('edit_poll_content', args=[poll_id]))
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
            return redirect(reverse('base_poll'))
    else:
        form = PollForm(instance=record)

    return render(request, 'poll/poll_form.html', {'form': form})


@login_required
@csrf_protect
def edit_question(request,question_id):
    data = get_object_or_404(Questions,id=question_id)

    if request.method == "POST":
        form = QuestionForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse('base_poll'))
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
        choise_list.append({
            'id': choise.id,
            'option': choise.option,
            'correct': choise.correct
        })

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
        return redirect(reverse('base_poll'))

    return redirect(reverse('base_poll'))


@login_required
@csrf_protect
def delete_question(request):

    if request.method == "POST":
        question_id = request.POST.get('questionID')
        record = get_object_or_404(Questions,id=question_id)
        poll_id = record.poll.id
        record.delete()
        return redirect(reverse('take_poll',args=[poll_id]))

    return redirect(reverse('base_poll'))


@login_required
@csrf_protect
def delete_choise(request):

    if request.method == "POST":
        choise_id = request.POST.get('choiseID')
        poll_id = request.POST.get('pollID')
        record = get_object_or_404(Choises,id=choise_id)

        record.delete()
        return redirect(reverse('edit_poll_content',args=[poll_id]))

    return redirect(reverse('base_poll'))


@login_required
@csrf_protect
def save_poll_results(request):
    if request.method == "POST":
        """ QueryDict converting to python dictionary """

        post_dict = request.POST.dict()
        obj_list = []

        # delete csrfmiddlewaretoken key for index converting
        if post_dict['csrfmiddlewaretoken']:
            del post_dict['csrfmiddlewaretoken']

        for key, value in post_dict.iteritems():
            please_int = key[-1]

            try:
                questiond = int(please_int, base=10)
                obj_list.append(Results(user=request.user, poll=1, question=questiond, answer=value))
            except ValueError:
                print("Cound't convert '{0}' to integer".format(please_int))
                raise Http404

        if obj_list:
            """ bulk create will perfor save """
            all_results = Results.objects.bulk_create(obj_list)

    return redirect(reverse('base_poll'))


def parse_result_object(result_obj):
    result_list = []

    for result in result_obj:
        result_list.append({
            'id': result.id,
            'poll': result.poll,
            'question': result.question,
            'answer': result.answer,
            'correct': False,
        })

    return result_list


@login_required
def get_user_statistic(request):
    data = Results.objects.filter(user=request.user)
    question_list = []

    result_list = parse_result_object(data)

    for result in result_list:
        # choises = Choises.objects.filter(Q(question=result['question']) & Q(correct=True))
        choises = Choises.objects.filter(question=result['question'])
        for choise in choises:
            question_list.append({
                'id': choise.id,
                'question_id': choise.question.id,
                'option': choise.option,
            })

            for result in result_list:
                if choise.id == result['answer']:
                    result['correct'] = choise.correct

    return render(request, 'poll/statistic.html', {'data': result_list, 'choises': question_list})

