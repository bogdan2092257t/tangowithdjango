from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says: hello world!<br/><a href='/rango/about/'>About</a>")
def about(request):
    return HttpResponse("This chapter has been put together by Bogdan Tufescu,2092257t<br/>Rango says this is the about page<br/><a href='/rango/'>Index</a>")
