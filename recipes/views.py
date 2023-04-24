from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def About(request):
    return HttpResponse('About 2')

def contact(request):
    return HttpResponse('contact 3')

