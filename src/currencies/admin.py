from django.contrib import admin
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('is_default', 'code', 'name', 'factor')
    list_display_links = ('code',)
    list_editable = ('factor', )
    
admin.site.register(Currency, CurrencyAdmin)
