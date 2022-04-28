from django.urls import path

from grid import views

urlpatterns = [
    path('', views.index, name='index'),
]
