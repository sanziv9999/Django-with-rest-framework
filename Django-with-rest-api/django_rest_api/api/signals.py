from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.management import call_command
from .models import Tours, TourDetails

@receiver(post_save, sender=Tours)
def run_collectstatic_after_tour_save(sender, instance, created, **kwargs):
    # Run collectstatic after saving a Tour instance
    call_command('collectstatic', '--noinput')

@receiver(post_save, sender=TourDetails)
def run_collectstatic_after_tour_details_save(sender, instance, created, **kwargs):
    # Run collectstatic after saving a TourDetails instance
    call_command('collectstatic', '--noinput')
