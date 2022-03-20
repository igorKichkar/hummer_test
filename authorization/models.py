from django.db import models
from django.core.validators import RegexValidator


class Profile(models.Model):
    phone_number = RegexValidator(
        regex=r'^\d{9,15}$',
        message="Phone number. Up to 15 digits allowed."
    )
    phone = models.CharField(
        validators=[phone_number], max_length=17)
    self_invite_code = models.CharField(max_length=8, blank=True)
    activated_invite_code = models.CharField(max_length=8, blank=True)
    authorization_code = models.IntegerField(max_length=6)
    activation_status = models.BooleanField(default=False)
