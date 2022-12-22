from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings  
from django.conf.urls.static import static

app_name = "api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('country_info/', views.CountryAPI.as_view()),
    path('country_info/<int:pk>/', views.CountryAPI.as_view()),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 