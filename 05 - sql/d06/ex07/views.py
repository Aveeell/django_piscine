from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import movies as m
from .models import Movies
from . import form
from django.views import View


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
    except Exception as err:
        return HttpResponse(err)
    return HttpResponse(str(i) + "<br>" for i in res)


def display(request):
    try:
        movies = Movies.objects.all()
        if len(movies) == 0:
            raise Movies.DoesNotExist
        return render(request, 'ex07/index.html', {"movies": movies})
    except Movies.DoesNotExist:
        return HttpResponse("No data available")


class Update(View):
    def get(self, request):
        try:
            movies = Movies.objects.all()
        except Movies.DoesNotExist as e:
            return HttpResponse("No data available movies")
        choices = ((movie.title, movie.title) for movie in movies)
        context = {"form": form.UpdateForm(choices)}
        return render(request, 'ex07/update.html', context)

    def post(self, request):
        try:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
        except Movies.DoesNotExist as e:
            return redirect(request.path)
        choices = ((movie.title, movie.title) for movie in movies)
        data = form.UpdateForm(choices, request.POST)
        if data.is_valid():
            try:
                movie = Movies.objects.get(title=data.cleaned_data['title'])
                movie.opening_crawl = data.cleaned_data['opening_crawl']
                movie.save()
            except Exception as err:
                return HttpResponse(err)
        return redirect(request.path)
