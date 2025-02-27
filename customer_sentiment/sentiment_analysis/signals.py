from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomerReview

@receiver(post_save, sender=CustomerReview)
def review_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New review added: {instance.text}")
