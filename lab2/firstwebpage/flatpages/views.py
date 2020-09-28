from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Привет, Мир!")#, content_type="text/plain; charset=UTF-8")

from django.shortcuts import render
from django import template
def home(request):
    return render(request, 'templates/index.html')

def final(request):
    return render(request, 'templates/static_handler.html')