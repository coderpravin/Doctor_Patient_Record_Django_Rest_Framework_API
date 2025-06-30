from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.DoctorView),
    path('patient', views.PatientView),

]