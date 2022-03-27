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

    if ls in response.user.todolist.all():
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(response, "list.html", {"ls": ls})
    return render(response, "view.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()
    return render(response, "create.html", {"form": form})


def view(response):
    return render(response, "view.html", {})


def contact(response):
    print(response.user, "was searches contact")
    return HttpResponse(f"<h1>No contact was given, sorry {response.user}</h1>"
                        f"<br></br><p>it's only a short information</p>")


"""Create API from using django"""


class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
