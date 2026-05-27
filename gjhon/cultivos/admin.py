from django.contrib import admin
from .models import Cultivo

@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'agricultor', 'zona', 'cantidad_sembrada', 'fecha_siembra')
    list_filter = ('zona',)
    search_fields = ('nombre', 'agricultor')
