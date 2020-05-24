from django.contrib import admin
# Register your models here.
from .models import Genre, News

admin.site.register(Genre)
#admin.site.register(News)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('header', 'image', 'article', 'slug', 'date', 'display_genere' )



