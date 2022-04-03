from xml.dom import ValidationErr


def validate_file_extension(archive):
    if not archive.name.endswith('.pdf'):
        raise ValidationError(u"Invalid archive type.")