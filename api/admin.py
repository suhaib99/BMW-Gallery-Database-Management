from django.contrib import admin
from .models import *


# Register your models here.
# want to access from administration panel 
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Employee)
admin.site.register(ThreeMFilm)
admin.site.register(Service)
admin.site.register(RepairOrder)
# admin.site.register(WorksOn)
admin.site.register(Req)