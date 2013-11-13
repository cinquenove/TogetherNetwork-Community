from storages.backends.s3boto import S3BotoStorage

STATICFILES_STORAGE = lambda: S3BotoStorage(bucket="static.togethernetwork.org")
DEFAULT_FILE_STORAGE = lambda: S3BotoStorage(bucket="media.togethernetwork.org")