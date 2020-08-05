from django import forms
from GFC_test.models import Article, Author

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'