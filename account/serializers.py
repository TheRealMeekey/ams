from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Profile


# class ProfileModelSerializer(ModelSerializer):

#     class Meta:
#         model = Profile
#         fields = '__all__'

# class UserModelSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ['location', 'phone', 'image']
        # exclude = ('user',)


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'profile'
        )

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(**profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        # Update User data
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        # Update UserProfile data
        if not instance.profile:
            Profile.objects.create(user=instance, **profile_data)
        instance.profile.location = profile_data.get('location', instance.profile.location)
        instance.profile.phone = profile_data.get('phone', instance.profile.phone)
        instance.profile.image = profile_data.get('image', instance.profile.image)
        instance.save()
        # Check if the password has changed

        return instance