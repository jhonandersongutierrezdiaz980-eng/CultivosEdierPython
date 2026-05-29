from django.urls import path
from .views import CultivoListView, CultivoCreateView, CultivoUpdateView, CultivoDeleteView

urlpatterns = [
    path('', CultivoListView.as_view(), name='cultivo_list'),
    path('nuevo/', CultivoCreateView.as_view(), name='cultivo_create'),
    path('editar/<int:pk>/', CultivoUpdateView.as_view(), name='cultivo_edit'),
    path('eliminar/<int:pk>/', CultivoDeleteView.as_view(), name='cultivo_delete'),
]
