from django.dispatch import receiver
from htmlparser.models import RawArchive
from django.db.models.signals import post_save

@receiver(post_save, sender=RawArchive)
def raw_archive_was_uploaded(sender, instance, **kwargs):
    handle_unzip(instance)    


def handle_unzip(raw_archive):
    pass