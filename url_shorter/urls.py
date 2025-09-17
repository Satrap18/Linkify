from django.urls import path, include
from url_shorter.views import ShorterView, ReturnRequestView, RedirectShortUrl
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'url', ShorterView, basename='url')


urlpatterns = [
    path('api/', include(router.urls)),
    path('', ReturnRequestView.as_view(), name='main'),
    path('<str:short_url>/', RedirectShortUrl.as_view(), name='redirect_short_url'),
]