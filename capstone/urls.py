
from django.contrib import admin
from django.urls import path, include

app_name = 'myband'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myband.urls')),
    path('user_auth/', include('django.contrib.auth.urls')),
    path('user_auth/', include('user_auth.urls')),
]
