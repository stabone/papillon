from django.forms import ModelForm

from courses.models import Categorie, Tut


class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        #TODO: attrs={'class':'ui form'} // there should be manualy created form

class TutForm(ModelForm):
    class Meta:
        model = Tut

