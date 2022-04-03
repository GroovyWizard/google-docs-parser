from htmlparser.models import RawArchive
from rest_framework import serializers 

class RawArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RawArchive
        fields = ['id', 'filename', 'file']