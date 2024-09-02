from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import RegexValidator

class Timer(models.Model):
    user = models.OneToOneField('Users', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Users(AbstractUser):
    is_paid = models.BooleanField(default=False, null=True, blank=True)
    username = models.CharField(max_length=11, unique=True, blank=True, null=True, validators=[RegexValidator(r'^\d{11}$', 'Enter a valid phone number with exactly 11 digits.')])
    name = models.CharField(max_length=1000, null=True, unique=True)
    email = models.TextField(unique=True, blank=True, null=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    activation_date = models.DateTimeField(null=True, blank=True)
    serial_number = models.PositiveIntegerField(unique=True, editable=False, null=True, blank=True)

    class Meta:
        ordering = ['serial_number']

    def save(self, *args, **kwargs):
        if not self.serial_number:
            last_record = Users.objects.all().order_by('serial_number').last()
            if last_record:
                self.serial_number = last_record.serial_number + 1
            else:
                self.serial_number = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Pot(models.Model):
    username = models.CharField(max_length=11, null=True, blank=True, unique=True)
    img = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return self.username

