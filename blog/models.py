from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое статьи')
    image = models.ImageField(upload_to='blog_images/', verbose_name='Изображение', null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
