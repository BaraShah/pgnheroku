from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data_entry/', views.add_data, name='form'),
    path('search/', views.search, name='search'),
    path('edit/<str:pk>', views.update_data, name='edit'),
    path('delete/<str:pk>', views.delete, name='delete'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)