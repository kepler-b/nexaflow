from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^.*$', views.serve_app, name='serve_app'),
]