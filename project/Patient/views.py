from django.shortcuts import render
from .models import patient, doctor
from django.http import JsonResponse
# Create your views here.

def PatientView(request):
    patients = list(patient.objects.all().values())
    return JsonResponse(patients, safe=False)

def DoctorView(request):
    doctors = list(doctor.objects.all().values())
    return JsonResponse(doctors, safe=False)

