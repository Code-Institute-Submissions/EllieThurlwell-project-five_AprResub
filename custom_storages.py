from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ tell django to use S3 when running collectstatic """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ tell django to use S3 when running collectstatic """
    location = settings.MEDIAFILES_LOCATION
