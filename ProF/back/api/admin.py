from django.contrib import admin

# Register your models here.
from .models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'parent')
    list_display_links = ('id','name', 'parent')
    search_fields = ('name', 'parent')
    list_per_page = 25
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'compare_price',
                    'price', 'quantity', 'sold', )
    list_display_links = ('id', 'name', )
    list_filter = ('category', )
    list_editable = ('compare_price', 'price', 'quantity', )
    search_fields = ('name', 'description', )
    list_per_page = 25



admin.site.register(Category)
admin.site.register(Product)