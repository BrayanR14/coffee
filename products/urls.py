from django.urls import path
from .views import ProductFormView, ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view(), name='list_product'),
    path('agregar/', ProductFormView.as_view(), name='add_product'),
    path('detalle/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
]