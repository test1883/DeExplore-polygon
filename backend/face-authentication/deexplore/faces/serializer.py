from rest_framework import serializers
from .models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ["name", "address", "username", "photo"]


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ["photo"]
