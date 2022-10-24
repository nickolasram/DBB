from django.urls import path
from . import views

urlpatterns = [
    path('design', views.design, name='design'),
    path('database', views.database, name='database'),
    path('roadmap', views.roadmap, name='roadmap'),
]