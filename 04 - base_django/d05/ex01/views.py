from django.shortcuts import render
from django.http import HttpResponse

def nav(request):
    return render(request, 'ex01/nav.html')

def display(request):
    return render(request, 'ex01/display.html')

def django(request):
    return render(request, 'ex01/django.html')

def templates(request):
    return render(request, 'ex01/templates.html')
# Create your views here.
