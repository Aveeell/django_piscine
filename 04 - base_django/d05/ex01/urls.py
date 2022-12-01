from django.urls import path
from . import views

urlpatterns = [
    path('display', views.display, name='display'),
    path('django', views.django, name='django'),
    path('templates', views.templates, name='templates'),
    path('', views.nav, name='nav'),
]
