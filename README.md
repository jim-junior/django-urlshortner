# Django URL Shortner

A set of utils to build custom fully-functional Django URL Shortner. This library helps you build a custom URL Shortner service for your project without relying on external services like [bitly](https://bitly.com/)

## Quick Start

### Installation

Django UrlShortner is available at the [Python Packaging Index](https://pypi.org/project/django-urlshortner/) so you can Install it using `pip`

```sh
pip install django-urlshortner
```
> Please dont mistake the spelling with `django-urlshortener` when installing. The name does not have an `e` in the word shortner. Its `django-urlshortner` not `django-urlshortener` 

After you should add the `urlshortner` app to your `INSTALLED_APPS` in `settings.py`

### Configuration

```py
INSTALLED_APPS = [
    # ....
    "urlshortner"
]
```

Then you migrate the models to your database

```sh
python3 manage.py migrate
```

Lastly add the routes to your URLConf in your `urls.py` of your project.

```py
url_patterns = [
    # ...
    path("r/", include("urlshortner.urls")),
]
```

Now you are good to go.

## Usage

The library provides a list of utils to create shortened urls.

To create a short version of a url use the `shorten_url` function from `urlshortner.utils` module

```py
# python3 manage.py shell
from urlshortner.utils import shorten_url

url_route = shorten_url(
    "https://github.com/jim-junior/django-urlshortner",
    is_permanent=False
)

print(url_route)
# >>> 0ee3f0
```
You can now navigate to you the route that you assigned to `urlshortner.urls` in your URLConf add the returned value att the end of the url. In this case it would be `http://localhost:8000/r/0ee3f0/` and this would redirect you to the right URL

Sometimes you want to create a custom URL. For example you want to create a short link for a blog about your new product and you want a url that is easy to remember. You can add this easily by adding the `value` argument to the `shorten_url` function

```py
from urlshortner.utils import shorten_url

url_route = shorten_url(
    "https://myblog.com/blog/2022/10/10/..../my-new-product",
    value="NewProduct"
    is_permanent=False
)
```
You can now navigate to `https://localhost/r/NewProduct` and It will redirect you
___

Licence MIT

Copyright ©  [Beingana JIm Junior](https://github.com/jim-junior), 2022