from django.conf import settings
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_owner/', views.add_owner_form),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
