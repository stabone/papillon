import json

from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from courses.models import Categories, Tuts, Materials
from courses.forms import CategoryForm, TutForm, MaterialForm


def index(request):
    data = Categories.objects.all().order_by('course')
    return render(request, 'course/index.html', {'data': data})


@login_required
@csrf_protect
def add_categorie(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/course/')
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
            return redirect('/course/')
    else:
        categorie = Categories.objects.get(id=categorie_id)
        tut = Tuts(category=categorie)
        form = TutForm(instance=tut)

    return render(request, 'course/tut_form.html', {'form': form})


@login_required
@csrf_protect
def add_material(request, tut_id):
    form = MaterialForm()
    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/course/')
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
            return redirect('/course/')
    else:
        form = CategoryForm(instance=data)

    return render(request, 'course/category_form.html', {'form': form})


@login_required
@csrf_protect
def edit_tut(request, tut_id):
    data = Tuts.objects.get(id=tut_id)
    if request.method == "POST":
        form = TutForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/course/')
    else:
        form = TutForm(instance=data)

    return render(request, 'course/tut_form.html', {'form': form})


@login_required
@csrf_protect
def edit_material(request):
    return render(request, 'course/material_form.html', {'form': None})


def show_categorie(request):
    data = Categories.objects.all()

    return render(request, 'course/show_categorie.html', {'data': data})


def show_tut(request,tut_id):
    current_path = request.get_full_path()
    request.session['last_url'] = current_path
    data = Tuts.objects.filter(category=tut_id)

    return render(request, 'course/show_tut.html', {'data': data, 'course': tut_id})


def show_material(request, tut_id):
    data = Materials.objects.filter(tut=tut_id)

    return render(request, 'course/show_material.html', {'data': data})


@login_required
@csrf_protect
def delete_categorie(request):
    if request.method == "POST":
        category_id = request.POST.get('categoryID');
        record = Categories.objects.filter(id=category_id)
        record.delete()
        return redirect('/course/')

    return redirect('/course/')


@login_required
@csrf_protect
def delete_tut(request):
    """ child (material) records should be delete to """
    if request.method == "POST":
        category_id = request.POST.get('categoryID')
        tut_id = request.POST.get('tutID')
        record = get_object_or_404(Tuts,id=tut_id)
        record.delete()
        return redirect('/course/show/{0}/tut/'.format(category_id))

    return redirect('/course/')


@login_required
@csrf_protect
def delete_material(request):
    if request.method == "POST":
        material_id = request.POST.get('materialID')
        record = Materials.objects.get(id=material_id)
        record.video.delete()
        record.delete()

        return redirect('/course/')

    return redirect('/course/')


def rate_tut(request):
    if request.method == "POST":
        response_data = {}
        try:
            tut_id = int(request.POST.get('tut_id'))
            level  = int(request.POST.get('level'))
        except ValueError:
            response_data['error'] = 'Illegal values'
            return HttpResponse(json.dumps(response_data),content_type='application/json')

        tut = get_object_or_404(Tuts, id=tut_id)
        rating = tut.rating + level
        times_rated = tut.times_rated + 1
        response_data['level'] = rating / times_rated
        response_data['rated'] = times_rated
        tut.rating = rating
        tut.times_rated = times_rated
        tut.save()
        return HttpResponse(json.dumps(response_data),content_type='application/json')
    else:
        print("this is get request")


# customized 404 error
def handler404(request):
    return render(request, '404.html')
