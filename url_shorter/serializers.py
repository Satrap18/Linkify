from rest_framework import serializers
from url_shorter.models import Shorter
import hashlib, base64
from url_shorter.models import Shorter

class ShorterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shorter
        fields = ['id', 'original_url', 'url']

    
    def validate_url(self, value):
        
        original_url = self.initial_data['original_url']
        url_hash = hashlib.sha256(original_url.encode('utf-8')).digest()
        base64_encoded = base64.urlsafe_b64encode(url_hash)
        short_code_bytes = base64_encoded[:8]
        return short_code_bytes.decode('utf-8').rstrip('=')