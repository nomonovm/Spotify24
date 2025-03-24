from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from rest_framework.decorators import action


class MyPaginationClass(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class QoshiqchiModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqchiSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['ism', 'davlat']
    ordering_fields = ['t_sana']
    pagination_class = MyPaginationClass

    @action(detail=True, methods=['get'])
    def albomlar(self, request, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, pk=pk)
        albomlar = Albom.objects.filter(qoshiqchi=qoshiqchi)
        serializer = AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def qoshiqlar(self, request, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, pk=pk)
        albomlar = Albom.objects.filter(qoshiqchi=qoshiqchi)
        qoshiqlar = Qoshiq.objects.filter(albom__in=albomlar)
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='qoshiq-qoshish')
    def qoshiq_qoshish(self, request, pk):
        qoshiqchi = get_object_or_404(Qoshiqchi, pk=pk)
        albom_id = request.data.get('albom')
        albom = get_object_or_404(Albom, id=albom_id, qoshiqchi=qoshiqchi)
        qoshiq_serializer = QoshiqSerializer(data=request.data)
        if qoshiq_serializer.is_valid():
            qoshiq_serializer.save(albom=albom)
            return Response({'success': True, 'message': "Qo'shiq qo'shildi!"}, status=201)
        return Response(qoshiq_serializer.errors, status=400)


class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['nom']
    ordering_fields = ['sana']
    pagination_class = MyPaginationClass

    @action(detail=True, methods=['get'])
    def qoshiqlar(self, request, pk):
        albom = get_object_or_404(Albom, pk=pk)
        qoshiqlar = albom.qoshiq_set.all()
        serializer = QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='qoshiq-qoshish')
    def qoshiq_qoshish(self, request, pk):
        albom = get_object_or_404(Albom, pk=pk)
        qoshiq_serializer = QoshiqSerializer(data=request.data)
        if qoshiq_serializer.is_valid():
            qoshiq_serializer.save(albom=albom)
            return Response({'success': True, 'message': "Qo'shiq qo'shildi!"}, status=201)
        return Response(qoshiq_serializer.errors, status=400)


class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['nom', 'janr']
    ordering_fields = ['davomiylik']
    pagination_class = MyPaginationClass

    @action(detail=True, methods=['get'])
    def albom(self, request, pk):
        qoshiq = get_object_or_404(Qoshiq, pk=pk)
        serializer = AlbomSerializer(qoshiq.albom)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def qoshiqchi(self, request, pk):
        qoshiq = get_object_or_404(Qoshiq, pk=pk)
        serializer = QoshiqSerializer(qoshiq.albom.qoshiqchi)
        return Response(serializer.data)
