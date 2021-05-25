from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reponse):
    return HttpResponse ("<h1>Welcome to my app</h1>")
