from django.contrib import admin
from Patient.models import patient, doctor

# Register your models here.

admin.site.register(patient)
admin.site.register(doctor)