from django.urls import path

from . import views

urlpatterns = [
    path('', views.temporary, name='temporary'),
]