from django.db import models

# Create your models here.

specialityDoctor = [
    ("Nephrologist", "Nephrologist"),
    ("Cardiologist", "Cardiologist"),
    ("Dentist", "Dentist"),
    ("Orthopedic", "Orthopedic"),
    ("Dermatologist", "Dermatologist")
]

class doctor(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50, choices=specialityDoctor)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Doctor Name : {self.fname} - Speciality in : {self.speciality}" 
    
genderPatient = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
]
class patient(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=genderPatient)
    email = models.EmailField(unique=True)
    doctor = models.ManyToManyField(doctor, related_name="patients")

    def __str__(self):
        doctorName = "".join([f"{doc.fname}" for doc in self.doctor.all()])
        return f"The patient name {self.fname} - Appointment with Doctor :{doctorName}"