from rest_framework import serializers
from Patient.models import patient, doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):

    doctor = serializers.PrimaryKeyRelatedField(queryset = doctor.objects.all(), many=True, write_only = True)
    doctor_details = DoctorSerializer(source='doctor', many=True, read_only=True)


    class Meta:
        model = patient
        fields = ['id', 'fname', 'lname', 'gender', 'email', 'doctor', 'doctor_details']

