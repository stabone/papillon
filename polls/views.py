from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import Http404


from polls.models import Polls, Questions, Answers
from polls.forms  import PollForm, QuestionForm, AnswerForm


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
    done_polls = Results.objects.select_related('user').filter(user=user_obj)
    valid_polls = []

    for record in done_polls:
        if record.poll in poll_dict:
            del poll_dict[record.poll]

    for key in poll_dict:
        valid_polls.append(poll_dict[key])

    return valid_polls
# plain python functions


def poll_list(request):
    poll_list = Polls.objects.all()
    return render(request, 'poll/list.html', {'polls': poll_list})


def poll_form(request):
    poll_form = PollForm()

    return render(request, 'poll/form.html',
                    {'form': poll_form,
                    'url_post_to': reverse_lazy('poll_create')})


@login_required
@csrf_protect
def poll_create(request):
    if request.method == "GET":
        return redirect(reverse_lazy('poll_form'))

    poll_form = PollForm(request.POST)

    if poll_form.is_valid():
        poll = poll_form.save(commit=False)
        poll.user = request.user
        poll.save()

        return redirect(reverse_lazy('poll_list'))

    return render(request, 'poll/form.html', {'form': poll_form})


def poll_edit(request, poll_id):
    poll = get_object_or_404(Polls, id=poll_id)
    poll_form = PollForm(instance=poll)

    return render(request, 'poll/form.html',
                    {'form': poll_form,
                    'record_id': poll.id,
                    'url_post_to': reverse_lazy('poll_update')})


def poll_update(request):
    if request.method == "POST":
        poll_id = request.POST.get('record', '')

        info = get_object_or_404(Polls, id=poll_id)
        poll = PollForm(request.POST, instance=info)

        if poll.is_valid():
            poll.save()

            return redirect(reverse_lazy('poll_list'))

    return render(request, 'poll/form.html', {'form': poll})


def get_questions_and_answers(poll_object):
    questions = Questions.objects.filter(poll=poll_object)

    record_list = []
    for question in questions:
        record_list.append({
            'id': question.id,
            'question': question.question,
            'answers': Answers.objects.filter(question=question)
        })

    return record_list


def poll_item(request, poll_id):
    poll = get_object_or_404(Polls, id=poll_id)
    questions = get_questions_and_answers(poll)

    return render(request, 'poll/item.html',
                            {'poll': poll,
                            'questions': questions})


def poll_correct(request, poll_id):
    poll = get_object_or_404(Polls, id=poll_id)
    questions = get_questions_and_answers(poll)

    return render(request, 'poll/create.html',
                            {'poll': poll,
                            'questions': questions})


def poll_delete(request):
    if request.method == 'GET':
        return redirect(reverse_lazy('poll_list'))

    poll_id = request.POST.get('record', '')
    data = get_object_or_404(Polls, id=poll_id)

    data.delete()

    return redirect(reverse_lazy('poll_list'))


""" question magic """
def question_list(request):
    questions = Questions.objects.all()

    return render(request, 'question/list.html', {'questions': questions})


def question_form(request, poll_id):
    if request.method == 'POST':
        return redirect(reverse_lazy('question_list'))

    poll = get_object_or_404(Polls, id=poll_id)
    question = Questions(poll=poll)
    question_form = QuestionForm(instance=question)

    return render(request, 'question/form.html',
                    {'form': question_form,
                    'poll_id': poll.id,
                    'url_post_to': reverse_lazy('question_create')})


def question_create(request):
    if request.method == 'GET':
        return redirect(reverse_lazy('question_list'))

    poll_id = request.POST.get('poll')
    question_form = QuestionForm(request.POST)
    if question_form.is_valid():
        question_form.save()

        return redirect(reverse_lazy('poll_item', args=[poll_id]))

    return render(request, 'question/form.html', {'form': question_form})


def question_edit(request, question_id):
    question = get_object_or_404(Questions, id=question_id)
    question_form = QuestionForm(instance=question)

    return render(request, 'question/form.html',
                    {'form': question_form,
                    'record_id': question.id,
                    'poll_id': question.poll.id,
                    'url_post_to': reverse_lazy('question_update')})


def question_update(request):
    if request.method == "POST":
        question_id = request.POST.get('record', '')

        poll_id = request.POST.get('poll')
        info = get_object_or_404(Questions, id=question_id)
        question_form = QuestionForm(request.POST, instance=info)

        if question_form.is_valid():
            question_form.save()

            return redirect(reverse_lazy('poll_item', args=[poll_id]))

    return render(request, 'question/form.html', {'form': question_form})


def question_delete(request):
    if request.method == 'GET':
        return redirect(reverse_lazy('question_list'))

    question_id = request.POST.get('record', '')
    data = get_object_or_404(Answers, id=question_id)

    data.delete()

    return redirect(reverse_lazy('question_list'))


""" answer magic """
def answer_list(request):
    answers = Answers.objects.all()

    return render(request, 'answer/list.html', {'answers': answers})


def answer_form(request, question_id):
    if request.method == 'POST':
        return redirect(reverse_lazy('question_list'))

    question = get_object_or_404(Questions, id=question_id)
    answer = Answers(question=question)
    answer_form = AnswerForm(instance=answer)

    return render(request, 'answer/form.html',
                    {'form': answer_form,
                    'poll_id': question.poll.id,
                    'url_post_to': reverse_lazy('answer_create')})


def answer_create(request):
    if request.method == "GET":
        return redirect(reverse_lazy('answer_form'))

    poll_id = request.POST.get('poll')
    answer_form = AnswerForm(request.POST)

    if answer_form.is_valid():
        answer_form.save()

        return redirect(reverse_lazy('poll_item', args=[poll_id]))

    return render(request, 'answer/form.html', {'form': answer_form})


def answer_edit(request, answer_id):
    answer = get_object_or_404(Answers, id=answer_id)
    answer_form = AnswerForm(instance=answer)

    return render(request, 'answer/form.html',
                    {'form': answer_form,
                    'record_id': answer.id,
                    'poll_id': answer.question.poll.id,
                    'url_post_to': reverse_lazy('answer_update')})


def answer_update(request):
    if request.method == "POST":
        answer_id = request.POST.get('record', '')
        poll_id = request.POST.get('poll')

        info = get_object_or_404(Answers, id=answer_id)
        answer = AnswerForm(request.POST, instance=info)

        if answer.is_valid():
            answer.save()

            return redirect(reverse_lazy('poll_item', args=[poll_id]))

    return render(request, 'answer/form.html', {'form': answer})


def answer_delete(request):
    if request.method == 'GET':
        return redirect(reverse_lazy('answer_list'))

    answer_id = request.POST.get('record', '')
    data = get_object_or_404(Answers, id=answer_id)

    data.delete()

    return redirect(reverse_lazy('answer_list'))


