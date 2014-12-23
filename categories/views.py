from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from categories.models import Categories
from categories.forms import CategoryForm


# category list
"""
class CategoryList(ListView):
    model = Categories
    template_name = 'categories/list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Categories.objects.all().order_by('title')
        return queryset


# add category
class CategoryCreate(CreateView):
    model = Categories
    template_name = ''

# edit category
# delete category
"""


def list(request):
    categories = Categories.objects.all().order_by('title')

    return render(request, 'category/list.html', {'categories': categories})


def show_form(request):

    categoryForm = CategoryForm()

    return render(request, 'category/category_form.html', {'form': categoryForm})


def add(request):
    if request.method == "GET":
        return redirect(redirect_lazy('category_show'))

    categoryForm = CategoryForm(request.POST)

    if categoryForm.is_valid():
        categoryForm.save()

        return redirect(reverse_lazy('category_list'))

    return render(request, 'category/category_form.html', {'form': categoryForm})


def edit(request, rec_id):
    category = get_object_or_404(Categories, id=rec_id)
    pass


def item(request, rec_id):
    pass


def delete(request):
    pass


