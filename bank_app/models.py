from django.db import models
from rest_framework import serializers


class Bank(models.Model):
    ifsc = models.CharField(max_length=12)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'
