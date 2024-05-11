from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import InstituitionSerializer
from rest_framework import generics

# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     #data = request.data
#     #instance = Instituition.objects.all().order_by("?").first()
#     serializer = InstituitionSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         instance = serializer.save()
#         print(serializer.data)
#         return Response(serializer.data)
#     return Response({"invalid":"Not a valid Data"}, status=400)

# class InstituitionListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Instituition.objects.all()
#     serializer_class = InstituitionSerializer
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#         return super().perform_create(serializer)

# class InstituitionDetailAPIView(generics.RetrieveAPIView):
#     queryset = Instituition.objects.all()
#     serializer_class = InstituitionSerializer


