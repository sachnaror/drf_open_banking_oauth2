from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # ✅ Ensure this is present
    path('api/', include('bank_api.urls')),  # ✅ Ensure your API URLs are correctly included
]
