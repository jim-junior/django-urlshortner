from django.shortcuts import render
from django.shortcuts import redirect
from .utils.http import HTTPTemporaryRedirect, HTTPPermanentRedirect, HTTPNotFound
from .utils.urls import shorten_url
from .models import Url


# A view that redirects to a given url by geting the url path from the <str> in the path
def redirect_to_url(request, short_url):
    try:
        url = Url.objects.get(short_url=short_url)
        if url.is_permanent:
            return HTTPPermanentRedirect(url.url)
        else:
            return HTTPTemporaryRedirect(url.url)
    except Url.DoesNotExist:
        return HTTPNotFound()
