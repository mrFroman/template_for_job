from django.contrib import admin
from .models import MenuTree, RegisterMenu


# категории меню в админке сайта
class RegisterMenuAdmin(admin.ModelAdmin):
    fields = ['name', 'verbose_name', ]
    list_display = ['__str__', ]


class MenuTreeAdmin(admin.ModelAdmin):
    fields = ['name', 'category', 'path', 'parent', ]
    list_display = ['__str__', 'category', 'path', 'parent', ]
    prepopulated_fields = {'path': ('name',)}


admin.site.register(RegisterMenu, RegisterMenuAdmin)
admin.site.register(MenuTree, MenuTreeAdmin)

