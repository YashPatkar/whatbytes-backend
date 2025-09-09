from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import DoctorModel, MappingModel, PatientModel
from .serializers import DoctorSerializer, MappingSerializer, RegisterUserSerializer, PatientSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model

user = get_user_model()
class RegisterUser(CreateAPIView):
    """
    Handle user registration and management. Users can sign up.
    """
    serializer_class = RegisterUserSerializer
    queryset = user.objects.all()

class Patient(ModelViewSet):
    """
    Manage patients in the system. you can view all patients, add new patients, update their details or remove a patient record.
    """
    serializer_class = PatientSerializer
    queryset = PatientModel.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class Doctor(ModelViewSet):
    """
    Manage doctors in the system. you can see all doctors, add new ones, update details or remove a doctor.
    """
    serializer_class = DoctorSerializer
    queryset = DoctorModel.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class Mapping(ModelViewSet):
    """
    Connect patients with doctors. You can list all mapping, create a new patient-doctor mapping or update and remove existing ones.
    """
    serializer_class = MappingSerializer
    queryset = MappingModel.objects.all()
    http_method_names = ['get', 'post', 'delete']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        """
        Created custom retrieve method so that for each patient we view all the doctors who are mapped to that patient.
        """
        patient_id = kwargs.get('pk')
        try:    
            mappings = MappingModel.objects.filter(patient_id=patient_id)
            doctors = [i.doctor for i in mappings]
            data = DoctorSerializer(doctors, many=True).data
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        
    def destroy(self, request, *args, **kwargs):
        """
        Delete a specific patient doctor mapping using mapping_id.
        """
        mapping_id = kwargs.get("pk")
        try:
                mapping = MappingModel.objects.filter(id=mapping_id).first()
                if mapping:
                    mapping.delete()
                    return Response({"detail": "Mapping deleted successfully."}, status=204)
                return Response({"detail": "Mapping not found."}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=400)