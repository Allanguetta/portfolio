from django.shortcuts import render
from .models import Portfolio

def home(request):
    posts = Portfolio.objects.all()
    context = {'posts' : posts}
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html')