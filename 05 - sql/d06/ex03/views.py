from django.http import HttpResponse
from django.shortcuts import render
from . import movies as m
from .models import Movies


def populate(request):
    res = []
    try:
        for i in m.movies:
            try:
                Movies.objects.create(
                    episode_nb=i['episode_nb'],
                    title=i['title'],
                    director=i['director'],
                    producer=i['producer'],
                    release_date=i['release_date'],
                )
                res.append('ok')
            except Exception as err:
                res.append(err)
                return HttpResponse(str(i) + "<br>" for i in res)
    except Exception as err:
        return HttpResponse(err)
    return HttpResponse(str(i) + "<br>" for i in res)


def display(request):
    try:
        movies = Movies.objects.all()
        if len(movies) == 0:
            raise Movies.DoesNotExist
        return render(request, 'ex03/index.html', {"movies": movies})
    except Movies.DoesNotExist:
        return HttpResponse("No data available")
