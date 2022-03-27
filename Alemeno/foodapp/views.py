from django.shortcuts import render, HttpResponse
# Create your views here.
def func(request):
    return HttpResponse("hello")