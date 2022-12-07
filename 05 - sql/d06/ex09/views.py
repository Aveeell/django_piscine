from django.http import HttpResponse
from django.shortcuts import render
from .models import People


def display(request):
    try:
        info = People.objects.filter(homeworld__climate__contains='windy').\
            values('name', 'homeworld__name', 'homeworld__climate').order_by('name')
        if len(info) == 0:
            raise People.DoesNotExist
        return render(request, 'ex09/display.html', {"info": info})
    except People.DoesNotExist as e:
        return HttpResponse("No data available")
