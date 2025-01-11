from django.contrib import admin
from news.models import News

class News_Admin (admin.ModelAdmin):
    list_display=("news_title","news_desc")

admin.site.register(News,News_Admin)    
# Register your models here.
