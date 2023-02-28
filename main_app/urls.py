
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('planes/', views.planes_index, name='index'),
    path('planes/<int:plane_id>/', views.plane_detail, name='detail'),
]
