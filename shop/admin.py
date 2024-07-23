from django.contrib import admin
from . models import *
# Register your models here.
class catagdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catagdmin)


class prodmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','price','stock','img']
    list_editable = ['price','stock','img']

admin.site.register(products,prodmin)