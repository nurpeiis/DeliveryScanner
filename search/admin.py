from django.contrib import admin
from .models import Pricedata
# Register your models here.
class PricedataAdmin(admin.ModelAdmin):
    list_display = ('dishname', 'restaurant')
admin.site.register (Pricedata, PricedataAdmin)