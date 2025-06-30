from django.urls import path
from PatientAPI.views import DoctorView, PatientView, PatientViewAPIMixin, DoctorViewAPIMixin, PatientDetailsAPIMixin, DoctorDetailsAPIMixin

from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename="doctor")

urlpatterns = [
    
    #This is Class Based View URLs
    path('doctorsView', DoctorView.as_view()),
    path('PatientView', PatientView.as_view()),

    #This is Mixins Generics View URLs
    path('PatientViewAPI', PatientViewAPIMixin.as_view()),
    path('DoctorViewAPI', DoctorViewAPIMixin.as_view()),
    path('PatientDetailsAPIMixin/<int:pk>', PatientDetailsAPIMixin.as_view()),
    path('DoctorDetailsAPIMixin/<int:pk>', DoctorDetailsAPIMixin.as_view()),
    

] + router.urls