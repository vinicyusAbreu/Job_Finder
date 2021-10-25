from django.contrib import admin
from .models import Emprego

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_vaga', 'empresa_contratante',)
    list_display_links = ('id', 'titulo_vaga', 'empresa_contratante',)


admin.site.register(Emprego, JobAdmin)
