from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.safestring import mark_safe
import django_filters

User = get_user_model()





class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])
    def get_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Sorter(models.Model):
    sorter = models.ForeignKey(Category, related_name='sorter', on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Фильтры'
        verbose_name_plural = 'Фильтры'

    def __str__(self):
        return self.name


class FirstCategory(models.Model):
    firstcategory = models.ForeignKey(Category, related_name='firstproducts', on_delete=models.CASCADE, )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Первая Категория'
        verbose_name_plural = 'Первая Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:first',
                       args=[self.slug])

class SecondCategory(models.Model):
    secondcategory = models.ForeignKey(FirstCategory, related_name='secondproducts', on_delete=models.CASCADE, )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Вторая Категория'
        verbose_name_plural = 'Вторая Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:second',
                       args=[self.secondcategory.firstcategory.slug, self.secondcategory.slug,self.slug])


class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE,)
    thirdcategory = models.ForeignKey(SecondCategory, related_name='thirdproducts', on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Search by name of product')
    price = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = ['price','name']




class Common(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название раздела', help_text='название основного раздела')
    slug = models.SlugField(null=True, unique=True, blank=True, verbose_name='URL адрес', help_text='название url адреса')
    mobile = models.BooleanField(verbose_name='Мобильная версия', help_text='поставить галочку если нужно в мобильной версии')

    class Meta:
        abstract = True

class Mainbar(Common):
    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Основное меню"
    def __str__(self):
        return self.name

class Subbar(Common):
    class Meta:
        verbose_name = "Подраздел"
        verbose_name_plural = "Подменю"

    subname = models.ForeignKey(Mainbar, on_delete=models.CASCADE, related_name="subbar", null=True, blank=True)
    def __str__(self):
        return self.name






class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Video(models.Model):
    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Много товаров"

    name_video = models.CharField(max_length=100, null=True, blank=True, verbose_name='товары ччч', help_text='просто текст про товары')
    url_video = models.URLField(null=True)
    di_video = models.TextField(null=True)
    date_video = models.DateTimeField(auto_now_add=True, null=True)
    likes_video = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True, unique=True)


    @property
    def videoplay(self):
        return mark_safe('<iframe width="100" height="50" src="' + self.url_video + '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

    def __str__(self):
        return self.name_video

class Comment(models.Model):
    class Meta:
        db_table = "Комментарии"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    text = models.TextField()
    likes = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
