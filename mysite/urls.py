from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls', namespace='mainpage')),
    path('blog/', include('blog.urls', namespace='blog')),
]
