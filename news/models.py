from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    anons = models.TextField('Анонс', max_length=250)
    full_text = RichTextUploadingField('Текст статьи')
    date = models.DateTimeField('Дата публикации')
    img = models.ImageField(help_text='150x150px', verbose_name='Ссылка картинки')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url
