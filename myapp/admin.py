

# Register your models here.
from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    # 定义要在后台展示出来的字段
    list_display = ('title', 'pub_date', 'modify_date')

admin.site.register(Article, ArticleAdmin)