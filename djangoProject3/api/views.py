from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from students.models import Teacher
from .serialzers import TeacherSerializer
from rest_framework.renderers import JSONRenderer

class TeacherList(APIView):

    def get(self, request, format=None):
       teachers = Teacher.objects.all()
       serializer = TeacherSerializer(teachers, many=True)
       return Response(serializer.data)