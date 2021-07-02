from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home page')


def products(request):
    return HttpResponse('Products page')


def customer(request):
    return HttpResponse('Customer page')
