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
        return render(request, 'ex05/index.html', {"movies": movies})
    except Movies.DoesNotExist:
        return HttpResponse("No data available")


class Remove(View):
    def get(self, request):
        try:
            movies = Movies.objects.all()
            remove_form = form.RemoveForm(choices=((i.title, i.title) for i in movies))
            return render(request, 'ex05/remove.html', {'form': remove_form})
        except Exception as err:
            return HttpResponse(err)

    def post(self, request):
        try:
            movies = Movies.objects.all()
            choices = ((i.title, i.title) for i in movies)
            remove_form = form.RemoveForm(choices, request.POST)
            if remove_form.is_valid():
                try:
                    Movies.objects.get(title=remove_form.cleaned_data['title']).delete()
                except Exception as err:
                    return HttpResponse(err)
            return redirect(request.path)
        except Exception as err:
            return HttpResponse(err)
