from django.forms import ModelForm

from courses.models import Categorie, Tut, Material


class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        #TODO: attrs={'class':'ui form'} // there should be manualy created form

class TutForm(ModelForm):
    class Meta:
        model = Tuts

class MaterialForm(ModelForm):
    class Meta:
        model = Materials
