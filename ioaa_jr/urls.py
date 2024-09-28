from django.conf import settings
from django.conf.urls.static import static
from django.urls import include,path
urlpatterns = [
    # Your URL patterns here
    path('',include('event_app.urls')),
    path('registrations/',include('registration.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
