from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Custom user model that uses email instead of username for login.
    Adds a name field and makes email the unique identifier.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

class PatientModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class DoctorModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    specialist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class MappingModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE, null=True, blank=True)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        patient_str = f"{self.patient.name} ({self.patient.id})"
        doctor_str = f"{self.doctor.name} ({self.doctor.id})"
        return f"mapping {self.id}: {patient_str} = {doctor_str}"