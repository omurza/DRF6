from rest_framework import serializers
from .models import *
class AutorSerializer(serializers.Serializer):
    class Meta:
        model=AughtorModel
        fields='__all__'

class BookSerializer(serializers.Serializer):
    class Meta:
        model=BookModel
        fields='__all__'

class GanreSerializer(serializers.Serializer):
    class Meta:
        model=GenreModel
        fields='__all__'