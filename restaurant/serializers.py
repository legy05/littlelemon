from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer (ModelSerializer):
    class Meta:
        model = User
        fields= ['url', 'username', 'email', 'groups']