from django.db import models

# Create your models here.



class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=18)

# verbose_name 的作用是显示在后台中,不写就显示字段名称
class Article(models.Model):
    title = models.CharField(verbose_name="标题", max_length=125)
    content = models.TextField(verbose_name='内容')

    pub_date = models.DateTimeField(verbose_name='发表时间', auto_now_add=True, editable=True)
    modify_date = models.DateTimeField(verbose_name='修改时间', auto_now=True, null=True)

    def __str__(self):
        return self.title