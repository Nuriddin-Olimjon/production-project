from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', include('api.v1.user.urls')),
    path('storage', include('api.v1.storage.urls')),
    path('supplier', include('api.v1.supplier.urls')),
    path('sales', include('api.v1.sales.urls')),
    path('finance', include('api.v1.finance.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
