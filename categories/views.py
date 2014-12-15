from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from categories.models import Categories


# category list
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

