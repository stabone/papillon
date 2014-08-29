import json
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from courses.models import Materials
from polls.models import Polls
from comments.models import MaterialComments, PollComments


# plaing pythond fuctions
def get_latvian_date(date_obj):
    return date_obj.strftime('%Y.%M.%d %H:%m:%s')

# plaing pythond fuctions


def index(request):
    return render(request, '', {})


def add_video_comments(request):

    if request.method == "POST":
        video_id = request.POST.get('videoID')
        comment = request.POST.get('comment')

        material = Materials.objects.get(id=video_id)
        obj = MaterialComments.objects.create(user=request.user,material=material,comment=comment)
        obj.save()

        response_data = parse_comments({
            'commentID': obj.id,
            'comment': obj.comment,
            'added': get_latvian_date(obj.created_at)
        })

        return HttpResponse(json.dumps(response_data), content_type='application/json')
        # return redirect(reverse('show_material',args=[video_id]))


def parse_comments(comment_dict):
    comments = []

    for comment in comment_dict:
            comments.append({
                'commentID': comment.id,
                'comment': comment.comment,
                'added': get_latvian_date(comment.created_at)
            })

    return comments


def get_poll_comments(request):
    if request.method == 'POST':
        poll_id = request.POST.get('pollID')

        try:
            poll_comments = PollComments.objects.filter(poll=poll_id)
            poll_data = parse_comments(poll_comments)
        except ValueError:
            response_data.append({'error': 'Komentāri netika atrasti'})

    return HttpResponse(json.dumps(poll_data), content_type='application/json')


def get_video_comments(request):

    if request.method == 'POST':
        video_id = request.POST.get('videoID')
        response_data = []

        try:
            id = int(video_id)
            comments = MaterialComments.objects.filter(material=id)
            response_data = parse_comments(comments)
        except ValueError:
            response_data.append({'error': 'Komentāri netika atrasti'})

    return HttpResponse(json.dumps(response_data), content_type='application/json')


def all_show_comments(request):
    data = MaterialComments.objects.all()
    return render(request, 'comment/show_comments.html', {'data': data})


@login_required
def add_poll_comments(request):
    if request.method == "POST":
        poll = request.POST.get('')
        comment = request.POST.get('')

        poll_obj = Polls.objects.get(id=poll)
        obj = PollComments.objecs.create(poll=poll_obj,comment=comment)
        obj.save()

        return render(request, '', {})

