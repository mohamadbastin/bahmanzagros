from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models, IntegrityError, transaction
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# from campaigns.models import CampaignPartyRelation
# from django.db.models.signals import post_save

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_len(value):
    if len(value) < 8:
        raise ValidationError(
            _('%(value)s is less than 8 characters.'),
            params={'value': value},
        )


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    # No other data for now


# @receiver(post_save, sender=User)
# def create_user_profile (sender, instance, **kwargs):
#
#     user_profile = UserProfile(user=instance)lsdjf lksjd lkdsj lkdsaj lksadj lksdjf ksdlf

#     user_profile.save()


@receiver(pre_save, sender=UserProfile)
def profile_usre_presave(sender, instance, **kwargs):
    # create user
    username = instance.username
    password = instance.password

    try:
        with transaction.atomic():
            the_user = User(username=username)
            the_user.set_password(password)

            the_user.save()
            instance.user = the_user

    except IntegrityError:
        pass

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


#post_save.connect(create_user_profile, sender=User)
