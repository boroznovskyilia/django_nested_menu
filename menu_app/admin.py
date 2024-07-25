from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url', 'tree_depth')
    readonly_fields = ('tree_depth', 'url')

admin.site.register(MenuItem, MenuItemAdmin)