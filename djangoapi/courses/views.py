from django.shortcuts import render
from rest_framework import viewsets
from . models import Courses
from . serializer import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer