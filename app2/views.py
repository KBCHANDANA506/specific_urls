from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Virat(request):
    return HttpResponse('<h1>Virat is the best batsman</h1>')

def jadeja(request):
    return HttpResponse('<h1>jadeja is a best player</h1>')