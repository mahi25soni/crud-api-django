from .serializers import StudentSerializer
from rest_framework import viewsets
from enroll.models import Student

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer