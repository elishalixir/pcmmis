from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse('Test PAGE')

def testpage(request):
    return HttpResponse('Test PAGE')
