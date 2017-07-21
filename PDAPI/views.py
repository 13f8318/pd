from django.shortcuts import render
from .models import Subjects
from rest_framework import viewsets
from .Serializers import SubjectsSerializers

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all().order_by('-date_created')
    serializer_class = SubjectsSerializers


# Create your views here.
