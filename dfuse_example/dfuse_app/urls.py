from django.urls import path
from . import views

urlpatterns = [
    path("dfuse-example/",  views.home),
]