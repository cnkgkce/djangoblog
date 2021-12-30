from django.contrib import admin
from .models import Article,Comment #. buradaki klasör demektir 


# Register your models here.


admin.site.register(Comment) #admin panelinde kaydettik. İlk model için bunu yazmaya gerek yoktu ama diğerleri için bunu yapmalıyız.


@admin.register(Article) #dahil ettiğimiz article modeli admin panelinde gösterilir
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]

    list_display_links = ["title","author","created_date"]

    search_fields = ["title"]

    list_filter = ["created_date"]
    
    class Meta: #Meta olmak zorunda
        model = Article




