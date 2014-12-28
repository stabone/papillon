from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from categories.models import Categories
from categories.forms import CategoryForm


def list(request):
    categories = Categories.objects.all().order_by('title')

    return render(request, 'category/list.html', {'categories': categories})


def form(request):

    category_form = CategoryForm()

    return render(request, 'category/form.html', {
                                    'form': category_form,
                                    'url_post_to': reverse_lazy('category_create')})


def create(request):
    if request.method == "GET":
        return redirect(reverse_lazy('category_form'))

    category_form = CategoryForm(request.POST)

    if category_form.is_valid():
        category_form.save()

        return redirect(reverse_lazy('category_list'))

    return render(request, 'category/form.html', {'form': category_form})


def edit(request, rec_id):
    category = get_object_or_404(Categories, id=rec_id)
    form = CategoryForm(instance=category)

    return render(request, 'category/create.html',
                                    {'form': form,
                                    'record_id': category.id,
                                    'url_post_to': reverse_lazy('category_update')})


def update(request):
    if request.method == "POST":
        category_id = request.POST.get('record', '')

        info = get_object_or_404(Categories, id=category_id)
        category = CategoryForm(request.POST, instance=info)

        if category.is_valid():
            category.save()

            return redirect(reverse_lazy('category_list'))

    return render(request, 'category/create.html', {'form': category})


def item(request, rec_id):
    pass


def delete(request):
    if request.method == 'GET':
        return redirect(reverse_lazy('category_list'))

    category_id = request.POST.get('record', '')
    data = get_object_or_404(Categories, id=category_id)

    data.delete()

    return redirect(reverse_lazy('category_list'))

