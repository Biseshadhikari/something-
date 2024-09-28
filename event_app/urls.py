from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your URL patterns here
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
