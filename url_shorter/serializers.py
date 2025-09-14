from rest_framework import serializers
from url_shorter.models import Shorter
import hashlib, base64
from url_shorter.models import Shorter

class ShorterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shorter
        fields = ['id', 'original_url', 'url']

    
    def validate_url(self, value):
        url = self.initial_data['original_url']
        h = hashlib.sha256(url.encode('utf-8')).digest()
        en = base64.urlsafe_b64encode(h)
        short_link = en[:8]
        return short_link.decode('utf-8').rstrip('=')