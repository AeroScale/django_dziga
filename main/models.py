from django.db import models

class FeedBack(models.Model):
    #Форма обратной связи
    name = models.CharField('Name model', max_length=120)
    email = models.EmailField('Email', max_length=120, blank=True, null=True)
    phone = models.CharField('Phone', max_length=15)
    description = models.CharField('Description', max_length=250, blank=True, null=True)
    product = models.CharField('Product', max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма безкоштовного прорахунку'

