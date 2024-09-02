from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path("csrf/", views.get_csrf_token, name="csrf"),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('reset-password', views.reset_password, name='reset_password'),
    path('change-password', views.change_password, name='change_password'),
    path("oauth/authorize", views.authorize, name="authorize"),
]