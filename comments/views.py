import json
from django.shortcuts import render
from django.http import HttpResponse

from courses.models import Materials
from polls.models import Polls
from comments.models import MaterialComments, PollComments


def index(request):
    return render(request, '', {})


def video_comments(request):
    if request.method == "POST":
        video_id = request.POST.get('videoID')
        comment = request.POST.get('comment')

        response_data = {}
        response_data['success'] = 'Comment added!!!'

        material = Materials.objects.get(id=video_id)
        obj = MaterialComments.objects.create(material=material,comment=comment)
        obj.save()

        return HttpResponse(json.dumps(response_data),mimetype='application/json')


def show_comments(request):
    data = MaterialComments.objects.all()
    return render(request, 'comment/show_comments.html', {'data': data})


def poll_comments(request):
    if request.method == "POST":
        poll = request.POST.get('')
        comment = request.POST.get('')

        poll_obj = Polls.objects.get(id=poll)
        obj = PollComments.objecs.create(poll=poll_obj,comment=comment)
        obj.save()

        return render(request, '', {})


