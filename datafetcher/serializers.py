from rest_framework import serializers
from .models import Fetch

class FetchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fetch
        fields = '__all__'