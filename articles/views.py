#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from articles.models import Articles, ArticleReviews
from categories.models import Categories
from articles.forms import ArticleForm
from comments.models import ArticleComments


## TODO
# for articles > markdown file would be nice
def get_articles(category_id):
    if not category_id:
        return Articles.objects.all()

    category = get_object_or_404(Categories, id=category_id)
    return Articles.objects.filter(category=category)


def index(request, page_numb=None, category=None):

    article_list = get_articles(category)

    paginator = Paginator(article_list, 10)

    try:
        article_slice = paginator.page(page_numb)
    except PageNotAnInteger:
        article_slice = paginator.page(1)
    except EmptyPage:
        article_slice = paginator.page(paginator.num_pages)

    return render(request, 'article/index.html', {'articles': article_slice})


@login_required
@csrf_protect
def add(request):
    if request.method == "POST":
        # save article
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()

            return redirect(reverse_lazy('article_item', args=[article.id]))
    else:
        article_form = ArticleForm()

    return render(request, 'article/add.html', {'form': article_form})


@login_required
@csrf_protect
def edit(request, article_id):
    if request.method == "GET":
        article = get_object_or_404(Articles, id=article_id)
        form = ArticleForm(instance=article)

    return render(request, 'article/edit.html', {'form': form, 'article_id': article_id})


@login_required
@csrf_protect
def update(request, article_id):

    if request.method == 'GET':
        return redirect(reverse_lazy('article_item', args=[article_id]))

    category_id = request.POST.get('id', '')
    info = get_object_or_404(Articles, id=category_id)
    # article = CategoryForm(request.POST, instance=info)
    article = ArticleForm(request.POST, instance=info)

    if article.is_valid():
        article.save()

        return redirect(reverse_lazy('article_item', args=[article_id]))

    return render(request, 'article/edit.html', {'form': article, 'article_id': article_id})


def item(request, article_id):

    article = get_object_or_404(Articles, id=article_id)
    comments = ArticleComments.objects.select_related('user').filter(article=article_id)
    comment_count = 0 if not comments else comments.count()

    return render(request, 'article/item.html', {
                                'article': article,
                                'comments': comments,
                                'comment_info': '{0} Komentāri'.format(comment_count)})


@login_required
@csrf_protect
def delete(request):
    if request.method == "POST":
        article_id = request.POST.get('article_id', '')

        article = get_object_or_404(Articles, id=article_id)
        article.delete()

    return redirect(reverse_lazy('article_base'))


@login_required
def list_review(request):
    if request.method == "GET":
        return redirect(reverse_lazy('article_base'))


@login_required
def add_review(request):
    if request.method == "GET":
        return redirect(reverse_lazy('article_base'))


@login_required
def edit_review(request):
    if request.method == "GET":
        return redirect(reverse_lazy('article_base'))


@login_required
def update_review(request):
    if request.method == "GET":
        return redirect(reverse_lazy('article_base'))


def delete_review(request):
    if request.method == "GET":
        return redirect(reverse_lazy('article_base'))

    article_id = request.POST.get('review_id')

    article = get_object_or_404(ArticleReviews, id=article_id)
    article.delete()

    return redirect(reverse_lazy('article_base'))

