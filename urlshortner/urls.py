
from django.urls import path
from .views import redirect_to_url


urlpatterns = [
    path('<str:short_url>', redirect_to_url, name='redirect_to_url'),
]
