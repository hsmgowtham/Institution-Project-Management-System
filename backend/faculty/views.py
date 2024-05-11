from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FacultySerializer
from rest_framework import generics
from .models import Faculty

# Create your views here.
class FacultyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)
    filterset_fields = FacultySerializer.Meta.fields


class FacultyDetailAPIView(generics.RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyUpdateAPIView(generics.UpdateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

class FacultyDestroyAPIView(generics.DestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)