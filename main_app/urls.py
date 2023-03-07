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
    path('planes/<int:plane_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('planes/<int:plane_id>/assoc_pilot/<int:pilot_id>/', views.assoc_pilot, name='assoc_pilot'),
    path('planes/<int:plane_id>/unassoc_pilot/<int:pilot_id>/', views.unassoc_pilot, name='unassoc_pilot'),
    path('pilots/', views.PilotList.as_view(), name='pilots_index'),
    path('pilots/<int:pk>/', views.PilotDetail.as_view(), name='pilots_detail'),
    path('pilots/create/', views.PilotCreate.as_view(), name='pilots_create'),
    path('pilots/<int:pk>/update/', views.PilotUpdate.as_view(), name='pilots_update'),
    path('pilots/<int:pk>/delete/', views.PilotDelete.as_view(), name='pilots_delete'),
]
