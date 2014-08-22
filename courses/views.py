import json

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q, Avg

from courses.models import Categories, Tuts, Materials, Rating
from courses.forms import CategoryForm, TutForm, MaterialForm

def parser_categories(record_objects):

    data = {}

    for rec in record_objects:
        first_char = rec.course[0].upper()
        data_rec = {'id': rec.id, 'course': rec.course}

        # add to key if it dosn't exists
        if first_char in data:
            data[first_char].append(data_rec)
        else:
            data[first_char] = [data_rec]

    return data


def index(request):
    records= Categories.objects.all().order_by('course')
    data = parser_categories(records)

    return render(request, 'course/index.html', {'data': data})


@login_required
@csrf_protect
def add_categorie(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('base_course'))
    else:
        form = CategoryForm()

    return render(request, 'course/category_form.html', {'form': form})


@login_required
@csrf_protect
def add_tut(request, categorie_id):
    form = TutForm()
    if request.method == "POST":
        form = TutForm(request.POST)
        if form.is_valid():
            rec = form.save(commit=False)
            rec.author = request.user
            rec.save()
            return redirect(reverse('show_tut', args=[categorie_id]))
    else:
        categorie = Categories.objects.get(id=categorie_id)
        tut = Tuts(category=categorie)
        form = TutForm(instance=tut)

    return render(request, 'course/add_tutorial.html', {'form': form})


@login_required
@csrf_protect
def add_material(request, tut_id):
    form = MaterialForm()

    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('show_material', args=[tut_id]))
    else:
        tut = Tuts.objects.get(id=tut_id)
        data = Materials(tut=tut)
        form = MaterialForm(instance=data)

    return render(request, 'course/material_form.html', {'form': form})


@login_required
@csrf_protect
def edit_categorie(request, categorie_id):
    data = Categories.objects.get(id=categorie_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse('base_course'))
    else:
        form = CategoryForm(instance=data)

    return render(request, 'course/edit_category.html', {'form': form})


@login_required
@csrf_protect
def edit_tut(request, tut_id):
    data = Tuts.objects.select_related().get(id=tut_id)

    if request.method == "POST":
        form = TutForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect(reverse('show_tut', args=[data.category.id]))
    else:
        form = TutForm(instance=data)

    return render(request, 'course/edit_tutorial.html', {'form': form})


@login_required
@csrf_protect
def edit_material(request):
    return render(request, 'course/material_form.html', {'form': None})


def show_categorie(request):
    data = Categories.objects.all()

    return render(request, 'course/show_categorie.html', {'data': data})


def show_tut(request, tut_id):
    current_path = request.get_full_path()
    data = Tuts.objects.filter(category=tut_id)

    statistics = Rating.objects.filter(tutorial=tut_id).aggregate(avg_val=Avg('rating'))
    avg_val = statistics['avg_val'] if statistics['avg_val'] else 0

    return render(request, 'course/show_tut.html', {
                                    'data': data,
                                    'course': tut_id,
                                    'rating': avg_val})


def show_material(request, tut_id):
    # for user and editor difering
    if request.user.is_superuser:
        data = Materials.objects.filter(Q(tut=tut_id) & Q(post=True))
    else:
        data = Materials.objects.filter(tut=tut_id)

    return render(request, 'course/show_material.html', {'data': data})


def show_video(request, material_id):
    video = Materials.objects.get(id=material_id)

    return render(request, 'course/item.html', {'video': video})


@login_required
@csrf_protect
def delete_categorie(request):
    if request.method == "POST":
        category_id = request.POST.get('categoryID');
        record = Categories.objects.filter(id=category_id)
        record.delete()
        return redirect(reverse('base_course'))

    return redirect(reverse('base_course'))


@login_required
@csrf_protect
def delete_tut(request):
    """ child (material) records should be delete to """
    if request.method == "POST":
        category_id = request.POST.get('categoryID')
        tut_id = request.POST.get('tutID')
        record = get_object_or_404(Tuts,id=tut_id)
        record.delete()

        return redirect(reverse('show_tut', args=[category_id]))

    return redirect(reverse('base_course'))


@login_required
@csrf_protect
def delete_material(request):
    if request.method == "POST":
        material_id = request.POST.get('materialID')
        record = Materials.objects.get(id=material_id)
        record.video.delete()
        record.delete()

        return redirect(reverse('base_course'))

    return redirect(reverse('base_course'))


def rate_tut(request, tut_id, rating):
    tut = Tuts.objects.get(id=tut_id)

    obj = Rating.objects.create(tutorial=tut_id, rating=rating)
    obj.save()

    return redirect(reverse('show_tut', args=[tut_id]))


def publish_video(request):
    if request.method == "POST":
        video_id = request.POST.get('videoID')
        action = request.POST.get('action')
        video = get_object_or_404(Materials, id=video_id)
        video.post = True if action == 'False' else False
        video.save()

        return redirect(reverse('show_video', args=[video_id]))

    return redirect(reverse('show_video', args=[video_id]))


# customized 404 error
def handler404(request):
    return render(request, '404.html')

