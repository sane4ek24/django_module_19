from django.contrib import admin
from .models import Buyer, Game, News


@admin.register(Buyer)
class Buyer(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')
    list_filter = ('balance', 'age')
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(Game)
class Game(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    search_fields = ('title',)
    list_per_page = 20


@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    list_filter = ('content',)
    search_fields = ('title',)
    list_per_page = 10