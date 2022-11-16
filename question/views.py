from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Question, Option
from .serializers import QuestionSerializer, OptionSerializer
# Create your views here.

class QuestionListCreateView(generics.ListCreateAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  permission_classes = [permissions.AllowAny]

class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
  permission_classes = [permissions.AllowAny]

class OptionListCreateView(generics.ListCreateAPIView):
  queryset = Option.objects.all()
  serializer_class = OptionSerializer
  permission_classes = [permissions.AllowAny]

class OptionDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Option.objects.all()
  serializer_class = OptionSerializer
  permission_classes = [permissions.AllowAny]