from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register('post', PostView, basename = 'post')

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', index),
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('user/me/', UserView.as_view({'get':'get_current_user'}))
]
