from rest_framework import generics
from .serializers import *


class QoshiqchiListCreateView(generics.ListCreateAPIView):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer


class QoshiqchiRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer


class QoshiqListCreateView(generics.ListCreateAPIView):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer

class QoshiqRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer