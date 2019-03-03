from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                related_name='profile')
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    is_supplier = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_stocker = models.BooleanField(default=False)
    temp_address = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} contact"

@receiver(post_save, sender=User)
def create_or_update_user_contact(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
