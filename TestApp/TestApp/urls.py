from django.conf.urls import handler404
from django.conf.urls import handler500
from django.conf.urls import handler403
from django.conf.urls import handler400
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('tours/', include('tours.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404='main.views.not_found'
handler500='main.views.not_serv'
handler403='main.views.not_found'
handler400='main.views.not_found'

