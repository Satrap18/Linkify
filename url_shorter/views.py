from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from url_shorter.models import Shorter
from url_shorter.serializers import ShorterSerializer
from django.views import View
import hashlib, base64
# Create your views here.

class ShorterView(viewsets.ModelViewSet):

    queryset = Shorter.objects.all()
    serializer_class = ShorterSerializer


class ReturnRequestView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "main.html")

    def post(self, request, *args, **kwargs):
            original_url = request.POST.get("original_url")
            url_hash = hashlib.sha256(original_url.encode('utf-8')).digest()
            base64_encoded = base64.urlsafe_b64encode(url_hash)
            short_code_bytes = base64_encoded[:8]
            short_code = short_code_bytes.decode('utf-8').rstrip('=')

            shorter, created = Shorter.objects.get_or_create(
                original_url=original_url,
                defaults={'url': short_code}
            )

            return render(
                request, 
                'main.html', 
                {'short_code': f'http://localhost:8000/{shorter.url}', "original_url": ""}
            )

class RedirectShortUrl(View):

    def get(self, request, short_url, *args, **kwargs):

        shorter_instance = get_object_or_404(Shorter, url=short_url)
        return redirect(shorter_instance.original_url)