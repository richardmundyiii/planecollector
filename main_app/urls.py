from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('planes/', views.planes_index, name='index'),
    path('planes/<int:plane_id>/', views.plane_detail, name='detail'),
    path('planes/create/', views.PlaneCreate.as_view(), name='planes_create'),
    path('planes/<int:pk>/update/', views.PlaneUpdate.as_view(), name='plane_update'),
    path('planes/<int:pk>/delete/', views.PlaneDelete.as_view(), name='plane_delete'),
    path('planes/<int:plane_id>/add_maintenance/', views.add_maintenance, name='add_maintenance')
]
