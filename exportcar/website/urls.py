from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('form_data/', views.form_data, name="form"),
    path('upload/', views.upload, name="upload"),
]
