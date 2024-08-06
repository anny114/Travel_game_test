from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('success/', views.success, name='success'),
]
