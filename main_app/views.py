from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def planes_index(request):
    return render(request, 'planes/index.html', {
        'planes': planes
    })

planes = [
    {'tailNumber': 'N3416TW', 'manufacturer': 'Cessna', 'model': '172', 'description': 'Some info here', 'year': 1989},
    {'tailNumber': 'N91H28Z', 'manufacturer': 'Cirrus', 'model': 'SR22', 'description': 'Some info here', 'year': 2002},
]