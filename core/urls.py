from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar/', QoshiqchiListCreateView.as_view(), name='qoshiqchi-list'),
    path('qoshiqchilar/<int:pk>/', QoshiqchiRetrieveUpdateDestroyAPIView.as_view(), name='qoshiqchi-detail'),
    path('qoshiqlar/<int:pk>/', QoshiqRetrieveUpdateDestroyAPIView.as_view(), name='qoshiq-detail'),
    path('qoshiqlar/', QoshiqListCreateView.as_view(), name='qoshiq-list'),
]
