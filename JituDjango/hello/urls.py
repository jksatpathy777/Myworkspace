from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("Jitendra", views.Jitendra, name="Jitendra"),
    path("Guda", views.Guda, name="Guda"),
    path("<str:name>", views.greet, name="greet")
]
