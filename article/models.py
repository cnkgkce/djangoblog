from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
from django.db.models.fields.related import ForeignKey


# Create your models here.

class Article(models.Model):
    author  = models.ForeignKey("auth.User",on_delete= models.CASCADE,verbose_name="Yazar") #user direk gelir, user silinirse cascade ile siler
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi") #güncel time alır
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin") #boş gelebilir

    def __str__(self):
        return self.title

#Burası aslında db de bizim için Article diye bir table oluşturur ve onu ilişkilendirir

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="makale",related_name="comments") #Foreign key gerekli bağlama işlemini yapıyor
    comment_author = models.CharField(max_length=50,verbose_name="author")
    comment_content = models.CharField(max_length=200,verbose_name="comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']


