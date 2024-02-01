from django.db import models


class Meter(models.Model):
    DIRECTION_TYPES = (
        ('L', 'L'),
        ('R', 'R'),
        ('Ln', 'ln')
    )
    uuid = models.CharField(max_length=36, primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    direction = models.CharField(choices=DIRECTION_TYPES, max_length=2, null=True, blank=True)
    center_distance = models.PositiveIntegerField(default=0)
    verification_interval = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MeterVerification(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
