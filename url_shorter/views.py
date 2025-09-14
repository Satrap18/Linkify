from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from url_shorter.models import Shorter
from url_shorter.serializers import ShorterSerializer
from django.views import View
# Create your views here.

class ShorterView(viewsets.ModelViewSet):

    queryset = Shorter.objects.all()
    serializer_class = ShorterSerializer


class ReturnRequestView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "main.html")