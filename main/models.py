from django.db import models
from django.contrib.auth.models import User

"""class for creating database"""


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


"""class for creating a website admin"""


class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='please enter keywords')
    price = models.DecimalField(max_digits=6, decimal_places=2)
