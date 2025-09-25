from django.test import TestCase
from url_shorter.models import Shorter
from django.db import IntegrityError
# Create your tests here.
class ShorterTestCase(TestCase):

    def setUp(self):
        Shorter.objects.create(original_url='https://github.com/satrap18', url='http://short.ly/abc123')

    def test_url_original(self):
        shorter = Shorter.objects.get(id=1)
        self.assertEqual(shorter.original_url, 'https://github.com/satrap18')

    def test_url_field(self):
        shorter = Shorter.objects.get(id=1)
        self.assertEqual(shorter.url, 'http://short.ly/abc123')
    
    def test_url_unique_constraint(self):
        with self.assertRaises(IntegrityError):
            Shorter.objects.create(original_url='https://example.com', url='http://short.ly/abc123')

    def test_blank_original_url_allowed(self):
        shorter = Shorter.objects.create(original_url='', url='http://short.ly/xyz456')
        self.assertEqual(shorter.original_url, '')

    def test_blank_url_allowed(self):
        shorter = Shorter.objects.create(original_url='https://example.com', url='')
        self.assertEqual(shorter.url, '')

    def test_str_method(self):
        self.assertEqual(str(Shorter.objects.get(id=1)), 'http://short.ly/abc123')