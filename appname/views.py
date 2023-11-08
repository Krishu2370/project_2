from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def krishna(request):
    return HttpResponse('<h1><marquee>hi krishna how are you?</h1><marquee>')
