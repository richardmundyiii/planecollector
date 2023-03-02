from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Plane
from .forms import MaintenanceForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def planes_index(request):
    planes = Plane.objects.all()
    return render(request, 'planes/index.html', { 'planes': planes })

def plane_detail(request, plane_id):
    plane = Plane.objects.get(id=plane_id)
    maintenance_form = MaintenanceForm()
    return render(request, 'planes/detail.html', { 'plane': plane, 'maintenance_form': maintenance_form })

def add_maintenance(request, plane_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maintenance = form.save(commit=False)
        new_maintenance.plane_id = plane_id
        new_maintenance.save()
    else: 
        print(form.errors.as_data())
        
    return redirect('detail', plane_id=plane_id)

class PlaneCreate(CreateView):
    model = Plane
    fields = '__all__'
    success_url = '/planes'

class PlaneUpdate(UpdateView):
    model = Plane
    fields = ['name', 'description']

class PlaneDelete(DeleteView):
    model = Plane
    success_url = '/planes'