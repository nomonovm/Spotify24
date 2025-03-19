from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from main.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="connact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()

router.register('qoshiqchi/', QoshiqchiModelViewSet)
router.register('albomlar/', AlbomModelViewSet)
router.register('qoshiqlar/', QoshiqModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger_format/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('qoshiqchilar/', QoshiqchiListCreateView.as_view(), name='qoshiqchi-list'),
    # path('qoshiqchilar/<int:pk>/', QoshiqchiRetrieveUpdateDestroyAPIView.as_view(), name='qoshiqchi-detail'),
    # path('qoshiqlar/<int:pk>/', QoshiqRetrieveUpdateDestroyAPIView.as_view(), name='qoshiq-detail'),
    # path('qoshiqlar/', QoshiqListCreateView.as_view(), name='qoshiq-list'),
]
