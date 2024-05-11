from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InstituitionSerializer
from rest_framework import generics
from .models import Instituition

# Create your views here.
class InstituitionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Instituition.objects.all()
    serializer_class = InstituitionSerializer
    def perform_create(self, serializer):
        serializer.save()
        #return super().perform_create(serializer)
    filterset_fields = InstituitionSerializer.Meta.fields


class InstituitionDetailAPIView(generics.RetrieveAPIView):
    queryset = Instituition.objects.all()
    serializer_class = InstituitionSerializer

class InstituitionUpdateAPIView(generics.UpdateAPIView):
    queryset = Instituition.objects.all()
    serializer_class = InstituitionSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

class InstituitionDestroyAPIView(generics.DestroyAPIView):
    queryset = Instituition.objects.all()
    serializer_class = InstituitionSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
