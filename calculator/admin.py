from .models import Element, Job, Norms
from django.contrib import admin

class ElementInline(admin.TabularInline):
    list_display = ['name','price',]
    model = Element.jobs.through

class TypeInline(admin.TabularInline):
    list_display = ['name']
    model = Element.type.through
    extra = 1

class TypeWallInline(admin.TabularInline):
    list_display = ['name']
    model = Element.typewall.through
    extra = 1

class MaterialInline(admin.TabularInline):
    model = Job.materials.through

class NormsInline(admin.TabularInline):
    model = Norms
    extra = 1
# class TypeInline(admin.TabularInline):
#     model = Type
#     extra = 1
#
class MaterialAdmin(admin.ModelAdmin):
    inlines = [
         NormsInline, MaterialInline

    ]




class ElementAdmin(admin.ModelAdmin):

    inlines = [
        ElementInline, TypeInline, TypeWallInline
    ]
    exclude = ('jobs','type', 'typewall')



class NormsAdmin(admin.ModelAdmin):
    list_display = ['product', 'job', 'norms']


admin.site.register(Norms, NormsAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(Job, MaterialAdmin)


