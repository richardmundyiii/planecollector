from django.contrib import admin
from .models import Plane, Maintenance

# Register your models here.
from .models import Plane

admin.site.register(Plane)

admin.site.register(Maintenance)