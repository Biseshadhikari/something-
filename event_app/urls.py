from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    # Your URL patterns here
    path('',index),
    path('contact',contact)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
