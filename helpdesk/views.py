
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class ExecutorListView(generics.ListCreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class ExecutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExecutorSerializer
    queryset = Executor.objects.all()


class ApplicationListView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()