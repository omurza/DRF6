from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins , viewsets
from .models import *
from .serializers import *
class BookApi(GenericViewSet,
             mixins.CreateModelMixin,
             mixins.ListModelMixin,
             mixins.RetrieveModelMixin,
             mixins.DestroyModelMixin,
             mixins.UpdateModelMixin):
    queryset=BookModel.objects.all()
    serializer_class=AutorSerializer
    