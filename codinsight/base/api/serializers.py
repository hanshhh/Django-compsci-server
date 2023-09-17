# Classes that take in a Python object and turn it into a Json object.
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
