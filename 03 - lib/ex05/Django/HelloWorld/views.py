from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('''
    <center>
    <div style="border-style: solid; border-radius: 25px; width: 50%">
    <h1>Hello World!</h1>
    <h2>Hello World!</h2>
    <h3>Hello World!</h3>
    <h4>Hello World!</h4>
    <h5>Hello World!</h5>
    <h6>Hello World!</h6>
    </div>
    </center>'''
    )
# Create your views here.
