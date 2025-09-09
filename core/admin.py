from django.contrib import admin
from .models import CustomUser, PatientModel, DoctorModel, MappingModel

admin.site.register(PatientModel)
admin.site.register(DoctorModel)
admin.site.register(MappingModel)
admin.site.register(CustomUser)