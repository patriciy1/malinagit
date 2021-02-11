from django.contrib.auth.models import User, Group

from django.dispatch import receiver
from django.db.models.signals import post_save

from home.models import Customer

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    group = Group.objects.get(name='customer')
    instance.groups.add(group)
    Customer.objects.create(user=instance, name=instance.username)

post_save.connect(create_profile, sender=User)

