#-*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from courses.models import Materials
from polls.models import Polls
from comments.models import MaterialComments, PollComments, ArticleComments
from articles.models import Articles


# plain pythond fuctions
def get_latvian_date(date_obj):
    return date_obj.strftime('%Y.%M.%d %H:%m:%s')


def parse_comments(comment_dict):
    comments = []

    for comment in comment_dict:
            comments.append({
                'commentID': comment.id,
                'comment': comment.comment,
                'added': get_latvian_date(comment.created_at)
            })

    return comments
# plain pythond fuctions


def index(request):
    return render(request, '', {})


def add_video_comments(request):

    if request.method == "POST":
        video_id = request.POST.get('videoID')
        comment = request.POST.get('comment')

        material = Materials.objects.get(id=video_id)
        obj = MaterialComments.objects.create(user=request.user, material=material, comment=comment)
        obj.save()

        response_data = parse_comments({
            'commentID': obj.id,
            'comment': obj.comment,
            'added': get_latvian_date(obj.created_at)
        })

        return HttpResponse(json.dumps(response_data), content_type='application/json')
        # return redirect(reverse('show_material',args=[video_id]))


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


def show_all_comments(request):
    data = MaterialComments.objects.all()

    return render(request, 'comment/show_comments.html', {'data': data})


@login_required
def add_poll_comments(request):
    response_data = []

    if request.method == "POST":

        try:
            poll_id = request.POST.get('pollID')
        except ValueError:
            response_data.append({'error': 'Nepareiz identifikātors'})
            return HttpResponse(response_data, content_type='application/json')

        comment = request.POST.get('comment')

        poll_obj = Polls.objects.get(id=poll_id)
        obj = PollComments.objecs.create(user=request.user, poll=poll_obj, comment=comment)
        obj.save()

        response_data.append({'success': 'Komentārs pievienots'})

    return HttpResponse(response_data, content_type='application/json')

@login_required
def add_article_comment(request):
    response_data = []
    if request.method == 'POST':

        try:
            article_id = request.POST.get('articleID')
            comment = request.POST.get('comment')
        except ValueError:
            response_data.append({'error': 'Raksts netika atrast'})
            return HttpResponse(response_data, content_type='application/json')

        article = get_object_or_404(Articles, id=article_id)
        obj = ArticleComments.objects.create(article=article, comment=comment)
        obj.save()

        response_data.append({'success': 'Komentārs pievienots'})
    return HttpResponse(response_data, content_type='application/json')


@login_required
def delete_article_comment(request):
    response_data = []
    if request.method == 'POST':
        comment_id = request.POST.get('commentID', '')
        comment = get_object_or_404(ArticleComments, id=comment_id)

        comment.delete()
        response_data.append({'success': 'Komentārs izdzēst'})

    return HttpResponse(response_data, content_type='application/json')

