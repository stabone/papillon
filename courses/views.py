from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from courses.models import Categories, Tuts, Materials
from courses.forms import CategoryForm, TutForm, MaterialForm


def index(request):
    data = Categories.objects.all()
    return render(request, 'course/index.html', {'data': data})


@csrf_protect
def add_categorie(request):
    form = CategoryForm()
    if(request.method == "POST"):
        form = CategoryForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        form = CategoryForm()

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
        categorie = Categories.objects.get(id=categorie_id)
        tut = Tuts(categorie_id=categorie)
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
        tut = Tuts.objects.get(id=tut_id)
        data = Materials(tut_id=tut)
        form = MaterialForm(instance=data)

    return render(request, 'course/add_material.html', {'form': form})


@csrf_protect
def edit_categorie(request, categorie_id):
    data = Categories.objects.get(id=categorie_id)
    if(request.method == "POST"):
        form = CategoryForm(request.POST, instance=data)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        form = CategoryForm(instance=data)

    return render(request, 'course/edit_categorie.html', {'form': form})


@csrf_protect
def edit_tut(request, tut_id):
    data = Tuts.objects.get(id=tut_id)
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
    data = Categories.objects.all()
    return render(request, 'course/show_categorie.html', {'data': data})


def show_tut(request, tut_id):
    current_path = request.get_full_path()
    request.session['last_url'] = current_path
    data = Tuts.objects.filter(categorie_id=tut_id)
    return render(request, 'course/show_tut.html', {'data': data, 'course': tut_id})


def show_material(request, tut_id):
    data = Materials.objects.filter(tut_id=tut_id)
    return render(request, 'course/show_material.html', {'data': data})


def delete_categorie(request, categorie_id):
    record = Categories.objects.filter(id=categorie_id)
    if(record.delete()):
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/course/')


def delete_tut(request, tut_id):
    record = Tuts.objects.filter(id=tut_id)
    if(record.delete()):
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/course/')


def delete_material(request, material_id):
    record = Materials.objects.filter(id=material_id)

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


