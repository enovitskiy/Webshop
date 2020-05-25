from django.contrib import admin
from .models import Video, Comment, Mainbar, Subbar, Category, Product, FirstCategory, SecondCategory,Sorter

class Menu(admin.StackedInline):
    model = Subbar
    extra = 0

@admin.register( Mainbar)
class Panel(admin.ModelAdmin):
    inlines = [Menu]

class ProductAdmi(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmi)


class ProductAdmin(admin.StackedInline):
    model = Product
    extra = 2
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}



class SecondCategoryAdmin(admin.ModelAdmin):
    inlines = [ProductAdmin]
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register( SecondCategory, SecondCategoryAdmin)


class FirstCategoryAdmin(admin.StackedInline):
    model = FirstCategory
    extra = 2
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    inlines = [FirstCategoryAdmin]
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class SorterAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Sorter, SorterAdmin)








class VideoInline(admin.StackedInline):
    model = Comment
    extra = 4
    readonly_fields = ['likes']

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    readonly_fields = ['likes_video']
    list_filter = ['date_video']
    list_display = ['name_video', 'videoplay']
    prepopulated_fields = {'name_video':["slug"]}

admin.site.register(Video, VideoAdmin)



# Register your models here.