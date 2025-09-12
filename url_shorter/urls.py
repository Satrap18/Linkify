from django.urls import path, include
from url_shorter.views import ShorterView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'url', ShorterView, basename='url')


urlpatterns = [
    path('', include(router.urls)),
]