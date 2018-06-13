from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ams.settings import DATE_FORMAT
import datetime
from django.utils import timezone

class ExecutorListView(generics.ListCreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer

class ApplicationCreateView(generics.ListCreateAPIView):
    # queryset = Application.objects.all()
    # serializer_class = ApplicationSerializer

     def post(self, request, format=None):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.author = request.user
            serializer.status = 'New'
            serializer.published_date = datetime.date.today()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationListView(APIView): #all application

    def get(self, request, format=None):
        applications = Application.objects.filter(status__in = ['New', 'In the work'])
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

class ApplicationDetailView(APIView): #application detail

    def get_object(self, pk):
        try:
            return Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        application = self.get_object(pk)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        application = self.get_object(pk)
        serializer = ApplicationSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        application = self.get_object(pk)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MyApplicationView(APIView): #My Application

    def get(self, request, format=None):
        owners = Executor.objects.filter(owner__username=request.user)
        owner_posts = Application.objects.filter(status = 'In the work', application_executor__in = owners)
        auth_posts = Application.objects.filter(author__username = request.user, 
                                                status__in = ['New', 'In the work'])
        serializer_owner = ApplicationSerializer(owner_posts, many=True)
        serializer_auth = ApplicationSerializer(auth_posts, many=True)
        return Response([serializer_owner.data, serializer_auth.data])

class HistoryApplicationView(APIView): #Application History

    def get(self, request, format=None):
        owners = Executor.objects.filter(owner__username=request.user)
        app_history_owners = Application.objects.filter(status = 'Complited', 
                                                        application_executor__in = owners)
        app_history_auths = Application.objects.filter(status = 'Complited', 
                                                    author__username = request.user)
        serializer_owner = ApplicationSerializer(app_history_owners, many=True)
        serializer_auth = ApplicationSerializer(app_history_auths, many=True)
        return Response([serializer_owner.data, serializer_auth.data])