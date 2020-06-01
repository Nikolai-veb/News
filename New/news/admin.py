from django.contrib import admin
# Register your models here.
from .models import Genre, News

admin.site.register(Genre)
#admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('header', 'image', 'article', 'date', 'display_genre', 'slug')
    list_filter = ('date', 'genre')
    prepopulated_fields = {"slug": ("header",)}



