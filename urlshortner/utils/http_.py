
from django.http.response import HttpResponseRedirectBase


class HTTPTemporaryRedirect(HttpResponseRedirectBase):
    status_code = 307

    def __init__(self, redirect_to):
        super().__init__(redirect_to)
        self['Cache-Control'] = 'no-cache'


class HTTPPermanentRedirect(HttpResponseRedirectBase):
    status_code = 301

    def __init__(self, redirect_to):
        super().__init__(redirect_to)
        self['Cache-Control'] = 'no-cache'


class HTTPNotFound(HttpResponseRedirectBase):
    status_code = 404

    def __init__(self):
        super().__init__('/404')
        self['Cache-Control'] = 'no-cache'
