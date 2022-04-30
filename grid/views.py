from django.http import HttpResponse
from django.shortcuts import render
import grid.settings.index


def index(request):
    tab = grid.settings.index.fc_grille()
    context = {
        "tab": tab
    }
    return render(request, 'grid/index.html', context)