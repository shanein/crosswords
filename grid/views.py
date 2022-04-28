from django.http import HttpResponse
from django.shortcuts import render

from grid.models import tab


def index(request):

    return render (request,
                   'grid/index.html',
                   {'tab', tab})