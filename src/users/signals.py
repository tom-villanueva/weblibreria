from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from users.models import Profile
from carrito.models import Carrito
User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
        carrito = Carrito(cliente=instance)
        carrito.save()
        #print('Se guardo el nuevo usuario')