from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('expenses/', include('expenses.urls')),
    path('income/', include('userincome.urls')),
    path('preferences/', include('userpreferences.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

