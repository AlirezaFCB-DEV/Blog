from django.db.models.signals import post_save , post_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile

User = get_user_model()

@receiver(post_save , sender=User)
def create_profile_for_user (sender , instance , created , **kwargs):
    if created :
        Profile.objects.create(user=instance)
        print(f"Profile created for {instance.email}")
    
@receiver(post_delete , sender=User)
def delete_profile_with_user (sender , instance , **kwargs) :
    try :
        instance.profile.delete()
        print(f"Profile deleted for {instance.email}")
    except :
        pass