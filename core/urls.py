from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("ask-ai", views.stream_opena_response, name="ask-ai"),
]
