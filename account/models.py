from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length = 4, blank = True, verbose_name = 'Кабинет')
    phone = models.CharField(max_length = 11, blank = True, verbose_name = 'Телефон')
    image = models.ImageField(blank=True, null = True, upload_to='user_images',
        default='user_images/default-user.png', verbose_name = 'Фотография')


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()