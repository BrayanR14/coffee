from django.urls import path
from .views import MyOrderView, CreateOrderProductView, RemoveOrderProductView

urlpatterns = [
    path('my-orden/', MyOrderView.as_view(), name='my_order'),
    path('agregar-producto/', CreateOrderProductView.as_view(), name='add_product'),
    path('quitar-producto/<int:pk>/', RemoveOrderProductView.as_view(), name='remove_product'),
]