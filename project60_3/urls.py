from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app60_3 import views  # Import the views from app60_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.resume_view, name='resume'),  # Set resume_view as the root URL
    path('resume/', include('app60_3.urls')),  # Optional: keep /resume/ URL as well
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
