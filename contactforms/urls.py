from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactFormView.as_view(), name='contact'),
    path('bugreport/', views.Bug_Form_View.as_view(), name='bugreport'),
]