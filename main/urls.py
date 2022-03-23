from django.urls import path, include
from . import views

from rest_framework import routers
from .views import ToDoListViewSet

router = routers.DefaultRouter()
router.register(r'todolist', ToDoListViewSet)


urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.database_list, name="index"),
    path("create/", views.create, name="create"),
    path("contact/", views.contact, name="contact"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

