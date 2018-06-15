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

class TicketCreateView(generics.ListCreateAPIView): #Ticket create

    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.author = request.user
            serializer.status = 'New'
            serializer.published_date = datetime.date.today()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Добавить разрешение на просмотр только овнерами
class TicketListView(APIView): #all Ticket

    def get(self, request, format=None):
        tickets = Ticket.objects.filter(status__in = ['New', 'In the work'])
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

class TicketDetailView(APIView): #Ticket detail

    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ticket = self.get_object(pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MyTicketView(APIView): #my Ticket

    def get(self, request, format=None):
        owners = Executor.objects.filter(owner__username=request.user)
        owner_posts = Ticket.objects.filter(status = 'In the work', ticket_executor__in = owners)
        auth_posts = Ticket.objects.filter(author__username = request.user, 
                                                status__in = ['New', 'In the work'])
        serializer_owner = TicketSerializer(owner_posts, many=True)
        serializer_auth = TicketSerializer(auth_posts, many=True)
        return Response([serializer_owner.data, serializer_auth.data])

class HistoryTicketView(APIView): #Ticket history

    def get(self, request, format=None):
        owners = Executor.objects.filter(owner__username=request.user)
        app_history_owners = Ticket.objects.filter(status = 'Complited', 
                                                        ticket_executor__in = owners)
        app_history_auths = Ticket.objects.filter(status = 'Complited', 
                                                    author__username = request.user)
        serializer_owner = TicketSerializer(app_history_owners, many=True)
        serializer_auth = TicketSerializer(app_history_auths, many=True)
        return Response([serializer_owner.data, serializer_auth.data])