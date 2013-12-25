from django.forms import ModelForm

from courses.models import Categorie, Tut


class CategorieForm(ModelForm):
    class Meta:
        model = Categorie

class TutForm(ModelForm):
    class Meta:
        model = Tut

