from django import forms
from django_markdown.widgets import MarkdownWidget
from articles.models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        exclude = ('user',)
        labels = {
            'title': 'Virsraksts',
            'article': 'Raksts'
        }
        widgets = {
            # 'article': MarkdownWidget(),
            'title': forms.TextInput(attrs={'autofocus': ''}),
            'article': forms.Textarea()
        }
