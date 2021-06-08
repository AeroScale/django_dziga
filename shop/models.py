from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class ProductWindow(models.Model):

    title = models.CharField(max_length=100, verbose_name='Наименование')
    windows_anons = models.TextField(max_length=250, verbose_name='Анонс')
    image = models.ImageField(verbose_name='Изображение')
    windows_full = RichTextUploadingField('Текст статьи')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Окна'
        verbose_name_plural = 'Окна'

def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url
