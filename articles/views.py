from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from articles.models import Articles
from articles.forms import ArticleForm
from comments.models import ArticleComments


## TODO
# for articles > markdown file would be nice

def index(request, page_numb=None):
    article_list = Articles.objects.all()

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
        articleForm = ArticleForm(request.POST)

        if articleForm.is_valid():
            article = articleForm.save(commit=False)
            article.user = request.user
            article.save()

            return redirect(reverse('article_item', args=[article.id]))
    else:
        articleForm = ArticleForm()

    return render(request, 'article/add.html', {'form': articleForm})


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
    if request.method == "POST":
        articleData = get_object_or_404(Articles, id=article_id)
        article = ArticleForm(request.POST, instance=articleData)

        if article.is_valid():
            article.save()

            return redirect(reverse('article_item', args=[article_id]))

    return render(request, 'article/edit.html', {'form': article, 'article_id': article_id})


@login_required
def item(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    comments = ArticleComments.objects.select_related('user').filter(article=article_id)

    return render(request, 'article/item.html', {
            'article': article,
            'comments': comments})


@login_required
@csrf_protect
def delete(request):
    if request.method == "POST":
        article_id = request.POST.get('article_id')

        article = get_object_or_404(Articles, id=article_id)
        article.delete()

    return redirect(reverse('article_base'))

