from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from PDAPI import views

router = routers.SimpleRouter()
router.register(r'pai', views.SubjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    ##########################################
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
    ##########################################
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
