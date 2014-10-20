#-*- coding: utf-8 -*-
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

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

""" varbūt ir nepieciešams flags priekš Javascript'a???"""


def index(request):
    return render(request, '', {})


def go_to_orig_video(video_id):
    return redirect(reverse('show_material', args=[video_id]))


def add_video_comments(request):

    if request.method == "POST":
        video_id = request.POST.get('videoID')
        comment = request.POST.get('comment')
        is_js = request.POST.get('isJS', '')

        if not comment: # if empty
            return go_to_orig_video(video_id)

        material = get_object_or_404(Materials, id=video_id)
        obj = MaterialComments.objects.create(user=request.user,
                                        material=material, comment=comment)
        obj.save()

        response_data = parse_comments({
            'commentID': obj.id,
            'comment': obj.comment,
            'added': get_latvian_date(obj.created_at)
        })

        if is_js:
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            return go_to_orig_video(video_id)


def get_poll_comments(request):
    if request.method == 'POST':
        try:
            poll_id = request.POST.get('pollID')
        except KeyError:
            raise Http404

        try:
            poll_comments = PollComments.objects.filter(poll=poll_id)
            poll_data = parse_comments(poll_comments)
        except ValueError:
            poll_data.append({'error': 'Komentāri netika atrasti'})

    return HttpResponse(json.dumps(poll_data), content_type='application/json')


def get_video_comments(request):

    if request.method == 'POST':
        try:
            video_id = request.POST.get('videoID')
        except KeyError:
            raise Http404

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
            poll_id = int(request.POST.get('pollID'))
        except KeyError:
            raise Http404
        except ValueError:
            response_data.append({'error': 'Nepareiz identifikātors'})
            return HttpResponse(response_data, content_type='application/json')

        comment = request.POST.get('comment')

        poll_obj = Polls.objects.get(id=poll_id)
        obj = PollComments.objecs.create(user=request.user, poll=poll_obj, comment=comment)
        obj.save()

        response_data.append({'success': 'Komentārs pievienots'})
        messages.success(request, 'Komentārs pievienots')

    return redirect(reverse('base_poll')) # uz poll


@login_required
def add_article_comment(request):
    response_data = []
    if request.method == 'POST':

        try:
            article_id = request.POST.get('articleID')
            comment = request.POST.get('comment')
        except KeyError:
            raise Http404
        except ValueError:
            raise Http404

        article = get_object_or_404(Articles, id=article_id)
        obj = ArticleComments.objects.create(
                                        user=request.user,
                                        article=article,
                                        comment=comment)
        obj.save()

        if True:
            messages.error(request, 'Komentārs tika pievienots')
            return redirect(reverse('article_item', args=[article_id]))

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


@login_required
def delete_video_comment(request):
    response_data = []

    if request.method == 'POST':
        video_id = request.POST.get('videoID', '')
        comment = get_object_or_404(VideoComments, id=video_id)

        comment.delete()

    return HttpResponse(response_data, content_type='application/json')

