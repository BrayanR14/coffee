from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, DeleteView

from .models import Order, OrderProduct
from .forms import OrderProductForm
from django.urls import reverse_lazy

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()

class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(is_active=True, user=self.request.user )

        form.instance.order = order
        form.instance.quantity = 1  
        form.save()
        return super().form_valid(form)

class RemoveOrderProductView(LoginRequiredMixin, DeleteView):
    model = OrderProduct
    template_name = 'orders/remove_order_product.html'
    success_url = reverse_lazy("my_order")

