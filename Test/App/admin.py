from django.contrib import admin
from .models import Formation
from django.utils.html import format_html

# Register your models here.
class FormtionAdmin (admin.ModelAdmin):
    def logo_tag(self, obj):
        return format_html('<img src="{}" style="width:30px; height:30px;" />'.format(obj.logo.url))

    logo_tag.short_description = 'logo'  
    list_display = ('titre', 'logo_tag', 'etat','categorie')

admin.site.register(Formation,FormtionAdmin)
