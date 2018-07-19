from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # path('stormer/', include('stormer.urls')),
    # path('flooder/', include('flooder.urls')),
    path('admin/', admin.site.urls),
    url(r'^', views.FrontendAppView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
