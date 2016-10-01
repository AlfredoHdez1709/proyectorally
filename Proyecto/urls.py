from django.conf.urls import url, include
from django.contrib import admin
from home import urls as homeUrls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(homeUrls, namespace="home")),
        url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
]
