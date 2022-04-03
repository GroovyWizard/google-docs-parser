from django.dispatch import receiver
from htmparser.models import RawArchive

@receiver(post_save, sender=RawArchive)
def raw_archive_was_uploaded(sender, instance, **kwargs):
    handle_unzip(instance)    


def handle_unzip(raw_archive):
    print(raw_archive)
