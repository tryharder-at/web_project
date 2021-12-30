from django.contrib import auth, messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import LookForm
from accounts.decorators import *


@login_required(login_url='accounts:login')
def new(request):
    form = LookForm()
    if request.method == 'POST':
        form = LookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogues:catalogue')

    context = {'form': form}
    return render(request, 'looks/new.html', context)


@login_required(login_url='accounts:login')
def update(request, pk):
    look = Look.objects.get(id=pk)
    form = LookForm(instance=look)
    if request.method == 'POST':
        form = LookForm(request.POST, instance=look)
        if form.is_valid():
            form.save()
            return redirect('catalogues:catalogue')

    context = {'form': form}
    return render(request, 'looks/new.html', context)


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def delete(request, pk):
    look = Look.objects.get(id=pk)
    if request.method == 'POST':
        look.delete()
        return redirect('catalogues:catalogue')

    context = {'look': look}
    return render(request, 'looks/delete.html', context)


@login_required(login_url='accounts:login')
def favourite(request, pk):
    look = Look.objects.get(id=pk)

    if look.favourite.filter(id=request.user.id).exists():
        look.favourite.remove(request.user)
    else:
        look.favourite.add(request.user)

    return redirect('looks:look', look.pk)


def look(request, pk):
    look = Look.objects.get(id=pk)
    apparels = look.apparels.all()

    is_favourite = False
    if look.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    context = {'look': look, 'apparel': apparels, 'is_favourite': is_favourite}
    return render(request, 'looks/look.html', context)
