from django.shortcuts import render
from django.http import HttpResponseRedirect
from djang.views.decorators.csrf import csrf_protect

from courses.models import Categorie, Tut, Material
from courses.forms import CategorieForm, TutForm, MaterialForm


def index(request):
    data = Categorie.objects.all()
    return render(request, 'course/index.html', {'data': data})


@csrf_protect
def add_categorie(request):
    form = CategorieForm()
    if(request.method == "POST"):
        form = CategorieForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        form = CategorieForm()

    return render(request, 'course/add.html', {'form': form})


@csrf_protect
def add_tut(request, categorie_id):
    form = TutForm()
    if(request.method == "POST"):
        form = TutForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        categorie = Categorie.objects.get(id=categorie_id)
        tut = Tut(categorie_id=categorie)
        form = TutForm(instance=tut)

    return render(request, 'course/add.html', {'form': form})


@csrf_protect
def add_material(request, tut_id):
    form = MaterialForm()
    if(request.method == "POST"):
        form = MaterialForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        tut = Tut.objects.get(id=tut_id)
        data = Material(tut_id=tut)
        form = MaterialForm(instance=data)

    return render(request, 'course/add_material.html', {'form': form})


@csrf_protect
def edit_categorie(request, categorie_id):
    data = Categorie.objects.get(id=categorie_id)
    if(request.method == "POST"):
        form = CategorieForm(request.POST, instance=data)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        form = CategorieForm(instance=data)

    return render(request, 'course/edit_categorie.html', {'form': form})


@csrf_protect
def edit_tut(request, tut_id):
    data = Tut.objects.get(id=tut_id)
    if(request.method == "POST"):
        form = TutForm(request.POST, instance=data)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        form = TutForm(instance=data)

    return render(request, 'course/edit_tut.html', {'form': form})


@csrf_protect
def edit_material(request):
    return render(request, 'course/edit_material.html', {'form': None})


def show_categorie(request):
    data = Categorie.objects.all()
    return render(request, 'course/show_categorie.html', {'data': data})


def show_tut(request, tut_id):
    current_path = request.get_full_path()
    request.session['last_url'] = current_path
    data = Tut.objects.filter(categorie_id=tut_id)
    return render(request, 'course/show_tut.html', {'data': data, 'course': tut_id})


def show_material(request, tut_id):
    data = Material.objects.filter(tut_id=tut_id)
    return render(request, 'course/show_material.html', {'data': data})


def delete_categorie(request, categorie_id):
    record = Categorie.objects.filter(id=categorie_id)
    if(record.delete()):
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/course/')


def delete_tut(request, tut_id):
    record = Tut.objects.filter(id=tut_id)
    if(record.delete()):
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/course/')


def delete_material(request, material_id):
    record = Material.objects.filter(id=material_id)

    # try:
    #     .delete(record.video.url)
    # except NotImplementedError:
    #     back_url = "/course/show/{}/material/".forma(material_id)
    #     return HttpResponseRedirect()

    if(record.delete()):
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/course/')


# customized 404 error
def handler404(request):
    return render(request, '404.html')


