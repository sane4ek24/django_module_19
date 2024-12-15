from django.contrib import admin
from .models import Buyer
from .models import Probnaya


@admin.register(Buyer)
class Buyer(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)



admin.site.register(Probnaya)