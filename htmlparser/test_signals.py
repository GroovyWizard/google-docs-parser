
from django.test import TestCase
from htmlparser.signals import *
from htmlparser.models import RawArchive

class TestSignals(TestCase):
    def test_zip_should_be_extracted_when_raw_archive_is_uploaded(self): 
       raw_archive = RawArchive.objects.create(filename="Test File")

        