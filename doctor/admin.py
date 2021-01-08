from django.contrib import admin
from .models import DoctorProfile,consultsRequest,Message,Prescription

admin.site.register((DoctorProfile,consultsRequest,Message,Prescription))
# Register your models here.
