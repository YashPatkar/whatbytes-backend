from rest_framework.serializers import ModelSerializer
from .models import DoctorModel, MappingModel, PatientModel
from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model()

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        "Create a new instance from validated data."
        validated_data['username'] = f"user{user.objects.count() + 1}"
        return user.objects.create_user(**validated_data)

class PatientSerializer(ModelSerializer):
    class Meta:
        model = PatientModel
        fields = ['name', 'age', 'description']

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = DoctorModel
        fields = ['name', 'age', 'specialist']

class MappingSerializer(ModelSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=PatientModel.objects.all(), write_only=True, source='patient'
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=DoctorModel.objects.all(), write_only=True, source='doctor'
    )
    class Meta:
        model = MappingModel
        fields = ["patient", "doctor", "created_at", "updated_at", "patient_id", "doctor_id"]