from django.contrib.auth.models import User, Group
from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Article
from .views import send_weekly_notifications

@receiver(post_save, sender=Article)
def send_notifications(sender, instance, created, **kwargs):
    if created:
        send_weekly_notifications(instance.category)

@receiver(post_save, sender=User)
def create_user_profile(instance, created):
    if created:
        UserProfile.objects.create(user=instance)
        group = Group.objects.get(name='authors')
        instance.groups.add(group)