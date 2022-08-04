=====
Django URL Shortner
=====

A set of utils to build custom fully-functional Django URL Shortner.


Quick start
-----------

1. Add "urlshortner" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'urlshortner',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('r/', include('urlshortner.urls')),

3. Run ``python manage.py migrate`` to create the Url models.