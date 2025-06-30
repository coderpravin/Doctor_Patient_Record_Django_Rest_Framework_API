from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import DoctorSerializer, PatientSerializer
from Patient.models import doctor, patient
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets
from .paginations import CustomPagination

# Create your views here.

class DoctorView(APIView):
    def get(self, request):
        doctors = doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Patient View Record
class PatientView(APIView):
    def get(self,reqquest):
        patients = patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        


#using Generics-Mixins
class PatientViewAPIMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = patient.objects.all()
    serializer_class = PatientSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class PatientDetailsAPIMixin(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = "pk"

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self,request, pk):
        return self.update(request, pk)
    
    def patch(self,request,pk):
        return self.partial_update(request,pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)


class DoctorViewAPIMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class DoctorDetailsAPIMixin(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = "pk"

    def get(self, request,pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk) 

    def patch(self,request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
    

#using viewSet
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = CustomPagination









    

