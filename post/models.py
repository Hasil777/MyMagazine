import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField('Название',max_length=20, null=True, blank=True)
    content = models.TextField('Контент', null=True, blank=True)
    image = models.ImageField(upload_to='post/%Y/%m/%d',blank=True,null=True)
    publisher = models.CharField('Publisher',max_length=20,null=True,blank=True)
    
    def get_absolute_url(self):
        return reverse("homeDetail", kwargs={"pk": self.pk})
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
class Comment(models.Model):
    post = models.OneToOneField(to=Post, on_delete=models.CASCADE, verbose_name='Пост',null=True,blank=True)
    user = models.CharField('Имя', max_length=20)
    text = models.TextField('Текст')
    date = models.DateField('Название', auto_now_add=True,null=True,blank=True)
    active = models.BooleanField('Активность', default=False)
    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарии'
    def __str__(self):
        return self.user
