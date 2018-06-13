from rest_framework import serializers
from .models import Application, Executor
from rest_framework.fields import CurrentUserDefault

class ExecutorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Executor
        fields = ['application', 'owner']


class ApplicationSerializer(serializers.ModelSerializer):
    application_executor = ExecutorSerializer(many=True)

    class Meta:
        model = Application
        fields = '__all__'

    def create(self, validated_data):
        executor_data = validated_data.pop('application_executor')
        application = Application.objects.create(**validated_data)
        for executor_data in executor_data:
            Executor.objects.create(application=application, *executor_data)
        return application

    def update(self, instance, validated_data):
        executor_data = validated_data.pop('application_executor')
        executor = (instance.application_executor).all()
        executor = list(executor)
        # instance.author = CurrentUserDefault()
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