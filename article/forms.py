from django.forms import ModelForm, fields
from .models import Article



class ArticleForm(ModelForm):
    
    class Meta:
        model = Article
        fields = ['title','content','article_image']

