from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'dpcmmis/home.html')

def testpage(request):
    return HttpResponse('Test PAGE')
