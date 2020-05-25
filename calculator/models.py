from django.db import models
from data.models import Product


class Common(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название типа',
                            help_text='название типа')

    class Meta:
        abstract = True


class Type(Common):
    class Meta:
        verbose_name = "Тип штукатурки"
        verbose_name_plural = "Тип штукатурки"

    def __str__(self):
        return self.name


class TypeWall(Common):
    class Meta:
        verbose_name = "Тип поверхности"
        verbose_name_plural = "Тип поверхности"

    def __str__(self):
        return self.name


class Job(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    norms = models.DecimalField(max_digits=10, decimal_places=2)
    materials = models.ManyToManyField(Product, related_name='materials', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Работы'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return self.name

class Norms(models.Model):
    product = models.ForeignKey(Product, related_name='product_norms', on_delete=models.CASCADE, null=True, blank=True )
    job = models.ForeignKey(Job, related_name='job_norms', on_delete=models.CASCADE, null=True,
                                      blank=True)
    type = models.ForeignKey(Type, related_name='type_norms', on_delete=models.CASCADE, null=True,
                            blank=True)
    typewall = models.ForeignKey(TypeWall, related_name='type_norms', on_delete=models.CASCADE, null=True,
                             blank=True)
    norms = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        ordering = ('product',)
        verbose_name = 'Нормы'
        verbose_name_plural = 'нормы'

    def __str__(self):
        return self.job.name



class Element(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    jobs = models.ManyToManyField(Job, related_name='process')
    type = models.ManyToManyField(Type, related_name='typematerial')
    typewall = models.ManyToManyField(TypeWall, related_name='typeelement')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Элементы'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.name

