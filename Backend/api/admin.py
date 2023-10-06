from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Post)
admin.site.register(ViewCount)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    list_per_page = 25

admin.site.register(Category,CategoryAdmin)