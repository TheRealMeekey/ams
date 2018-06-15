from rest_framework import serializers
from .models import Ticket, Executor
from rest_framework.fields import CurrentUserDefault

class ExecutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Executor
        fields = ['ticket', 'owner']


class TicketSerializer(serializers.ModelSerializer):
    ticket_executor = ExecutorSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ['id', 'author', 'title', 'text', 'cabinet', 'phone', 'status', 'published_date', 'ticket_executor']

    def create(self, validated_data):
        author = self.author
        executor_data = validated_data.pop('ticket_executor')
        ticket = Ticket.objects.create(author=author, **validated_data)
        for executor_data in executor_data:
            Executor.objects.create(ticket=ticket, *executor_data)
        return ticket

    def update(self, instance, validated_data):
        executor_data = validated_data.pop('ticket_executor')
        executor = (instance.ticket_executor).all()
        executor = list(executor)
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.cabinet = validated_data.get('cabinet', instance.cabinet)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.status = validated_data.get('satus', instance.status)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        for executor_data in executor_data:
            executor = executor.pop(0)
            executor.owner = executor_data.get('owner', executor.owner)
            executor.save()
        return instance