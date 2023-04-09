from django.http import HttpResponse
from django.shortcuts import render


def sobre(request):
    return HttpResponse("sobre")


def home(request):
    return render(request, 'recipes/pages/home.html')
