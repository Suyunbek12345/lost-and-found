from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/v1/accounts/', include('account.urls')),
    path('api/v1/table/', include('table.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

