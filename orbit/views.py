from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
