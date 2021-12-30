from django.shortcuts import render
# Create your views here.
from looks.models import Look
from looks.filters import LookFilter


def catalogue(request):
    looks = Look.objects.all()

    context = {'looks': looks}
    return render(request, 'catalogues/catalogue.html', context)


def favourites(request):
    user = request.user
    looks = user.favourite.all()

    context = {'looks': looks}
    return render(request, 'catalogues/favourites.html', context)


def search(request):
    looks = Look.objects.all()

    lookFilter = LookFilter(request.GET, queryset=looks)
    looks = lookFilter.qs

    context = {'lookFilter': lookFilter, 'looks': looks}
    return render(request, 'catalogues/search.html', context)
