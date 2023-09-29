from django.contrib import admin

from ecoshop_app.models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','available','stock','created','updated']
    list_editable = ['available','price','stock']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
