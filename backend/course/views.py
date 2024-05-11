from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CourseSerializer
from rest_framework import generics
from .models import Course

# Create your views here.
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def perform_create(self, serializer):
        serializer.save()
        return super().perform_create(serializer)
    
    filterset_fields = CourseSerializer.Meta.fields


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseUpdateAPIView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

class CourseDestroyAPIView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)