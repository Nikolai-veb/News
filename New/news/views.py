from django.shortcuts import render
# Create your views here.
from .models import Genre, News
from django.views import generic


def index(request):
    genres = Genre.objects.all()
    news = News.objects.all()
    return render(request, 'index.html', context = {'genres':genres, 'news':news})

class NewsListView(generic.ListView):
    model = News
    padinate_by = 10

class NewDetailView(generic.DetailView):
    model = News
