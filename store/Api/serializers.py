from rest_framework import serializers
from .models import Clothes, Cart


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
