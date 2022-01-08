from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class =  serializers.QuestionSerializer
