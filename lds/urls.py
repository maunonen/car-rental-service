

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import i18n
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('i18n/', include(i18n)), 
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('rentals/', include('rentals.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" urlpatterns += i18n_patterns (
    path('', include('pages.urls')),
    prefix_default_language=True, 
)  """
