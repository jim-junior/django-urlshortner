# Django URL Shortner

A set of utils to build custom fully-functional Django URL Shortner.

## Quick start

1. Add `"urlshortner"` to your INSTALLED_APPS setting like this:

```py
INSTALLED_APPS = [
    ...
    'urlshortner',
]
```

Include the polls URLconf in your project urls.py like this:

```py
    path('r/', include('urlshortner.urls')),
```

1. Run `python manage.py migrate` to create the Url models.