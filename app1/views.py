from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('<h1>Mr.cool is the best finisher in the world</h1>')


def pandya(request):
    return HttpResponse('<h1>Pandya is allrounder</h1>')

