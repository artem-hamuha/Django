from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(reponse, name):
    ls = ToDoList.objects.get(name=name)
    return HttpResponse ("%s" %ls.name)
