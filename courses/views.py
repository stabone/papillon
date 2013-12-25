from django.shortcuts import render
from django.http import HttpResponseRedirect

from courses.models import Categorie, Tut
from courses.forms import CategorieForm, TutForm

def index(request):
    data = Categorie.objects.all()
    return render(request, 'course/index.html', {'data': data})

def add_categorie(request):
    form = CategorieForm()
    if(request.method == "POST"):
        form = CategorieForm(request.POST)
        if( form.is_valid() ):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        form = CategorieForm()

    return render(request, 'course/add.html', {'form': form})

def add_tut(request):
    form = TutForm()
    if(request.method == "POST"):
        form = TutForm(request.POST)
        if( form.is_valid() ):
            form.save()
            return HttpResponseRedirect('/course/')
    else:
        form = TutForm()

    return render(request, 'course/add.html', {'form': form})

def edit_categorie(request, categorie_id):
    data = Categorie.objects.filter(categorie_id)
    return render(request, 'course/edit_categorie.html', {'data': data})

def edit_tut(request, tut_id):
    data = Tut.objects.filter(tut_id)
    return render(request, 'course/edit_tut.html', {'data': data})

def show_categorie(request):
    data = Tut.objects.filter(tut_id)
    return

def show_tut(request, tut_id):
    data = Tut.objects.filter(tut_id)
    return

def delete_categorie(request, categorie_id):
    record = Categorie.objects.filter(id=categorie_id)
    if( record.delete() ):
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/course/')

def delete_tut(request, tut_id):
    record = Tut.objects.filter(id=tut_id)
    if( record.delete() ):
        return HttpResponseRedirect('/course/')

    return HttpResponseRedirect('/course/')

# customized 404 error
def handler404(request):
    return render(request, '404.html')
