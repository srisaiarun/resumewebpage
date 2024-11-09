from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app60_3 import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', views.resume_view, name='resume'),  # Home page for displaying the resume
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
