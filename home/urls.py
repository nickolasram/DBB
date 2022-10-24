from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('joins/', views.joins, name='joins'),
    path('columns/', views.columns, name='columns'),
    path('tables/', views.tables, name='tables'),
    path('order/', views.order, name='order'),
    path('hughjackman/', views.flush, name='flush'),
]