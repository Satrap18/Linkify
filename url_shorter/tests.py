from django.test import TestCase
from url_shorter.models import Shorter
# Create your tests here.
class ShorterTestCase(TestCase):

    def setUp(self):
        print("setUp: Run once for every test method to set up clean data.")
        Shorter.objects.create(original_url='https://github.com/satrap18')

    
    def test_url_original(self):
        original_urls = Shorter.objects.get(id=1)
        self.assertEqual(original_urls.original_url, 'https://github.com/satrap18')
