from django.db import models
from django.urls import reverse # Used to generate URls by reversing the URL patterns
import PIL

# Create your models here.
class Genre(models.Model):
    """Model representing a news ganre."""
    name = models.CharField(max_length=200, help_text='Enter a news genre')


    def __str__(self):
        """String for representing the Model object."""
        return self.name


class News(models.Model):
    """Model representing a news (but not a spec)"""
    header = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this news')
    image =  models.ImageField()
    article = models.TextField(help_text='Enter article')
    slug = models.SlugField(verbose_name='URL', blank=True)
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.header
    def get_absolute_url(self):
        return reverse('news-detail',args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'

