from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as TokenViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App_Main.urls')),
path('auth/', include('App_User.urls')),
    path('wsc/', include('App_WSC.urls')),
    path('api/', include('App_API.urls')),
    path("api/auth", TokenViews.obtain_auth_token, name="obtain_auth_token"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

