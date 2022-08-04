from ..models import Url
from django.conf.global_settings import SECRET_KEY
import hashlib
import time
import random
import string


def create_short_url_id(url):
    """
    Create a short url for the given url.
    """
    short_url = create_url_hash(url)
    while Url.objects.filter(short_url=short_url).exists():
        short_url = create_url_hash(url)
    return short_url


# Create a hash string of 7 characters for a given url encrypted with the SECRET_KEY and current time.
def create_url_hash(url):
    """
    Create a hash string of 7 characters for a given url encrypted with the SECRET_KEY and current time.
    """
    hash_string = hashlib.sha256(url.encode(
        'utf-8') + str(time.time()).encode('utf-8') + SECRET_KEY.encode('utf-8')).hexdigest()
    return hash_string[:7]


def shorten_url(url, is_permanent=False):
    """
    Shorten a given url.
    """
    short_url = create_short_url_id(url)
    urlObj = Url(url=url, short_url=short_url, is_permanent=is_permanent)
    urlObj.save()
    return urlObj.short_url
