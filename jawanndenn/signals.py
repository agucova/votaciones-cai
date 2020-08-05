from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.account.signals import user_logged_in, user_signed_up
from django.contrib.auth.models import User
from jawanndenn.models import Profile


@receiver(user_signed_up)
def cleanCapitalization(request, user, **kwargs):
    print("Caps for", user.email)
    user.first_name = user.first_name.capitalize()
    user.last_name = user.last_name.capitalize()
    user.save()