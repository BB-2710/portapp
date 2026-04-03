from django.urls import path
from .views import feedback_view
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("feedback/",feedback_view, name="feedback")
]