from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import ToDoList, Item
from .forms import CreateNewList

from rest_framework import viewsets
from .serializer import ToDoListSerializer, ItemSerializer


"""Typical views for django"""


def home(response):
    return render(response, "home.html", {})


def database_list(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "list.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "create.html", {"form": form})


def contact(response):
    print(response.user, "was searches contact")
    return HttpResponse(f"<h1>No contact was given, sorry {response.user}</h1>"
                        f"<br></br><p>it's only a short information</p>")


"""Create API from using django"""


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
