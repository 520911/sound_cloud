from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    return f'avatar/{instance.id}/{file}'


def validate_size_avatar(file):
    limit = 2
    if file.size > limit * 1024 * 1024:
        raise ValidationError(f'Max file size = {limit}MB')
