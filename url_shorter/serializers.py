from rest_framework import serializers
from url_shorter.models import Shorter
import hashlib, base64
from url_shorter.models import Shorter

class ShorterSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = Shorter
        fields = ['id', 'original_url', 'short_url']
        
    def get_short_url(self, obj):
        request = self.context.get('request')
        base_url = request.build_absolute_uri('/') if request else 'http://localhost:8000/'
        return f"{base_url}{obj.url}"

    def create(self, validated_data):
        original_url = validated_data['original_url']

        url_hash = hashlib.sha256(original_url.encode('utf-8')).digest()
        base64_encoded = base64.urlsafe_b64encode(url_hash)
        short_code_bytes = base64_encoded[:8]
        short_code = short_code_bytes.decode('utf-8').rstrip('=')

        shorter, created = Shorter.objects.get_or_create(
            original_url=original_url,
            defaults={'url': short_code}
        )
        return shorter

