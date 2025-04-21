from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女"),
    ("secret", "保密"),
)


class Person(models.Model):
    name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="secret")
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name

