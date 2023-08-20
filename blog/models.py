from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.CharField(max_length=200, unique=True)
    content = models.TextField(verbose_name='Содержание')
    preview_image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Публиковать?')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
