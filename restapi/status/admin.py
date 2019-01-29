from django.contrib import admin
from .models import Order
from .forms import OrderForm


class OrderAdmin(admin.ModelAdmin):
    list_display = ['description', "__str__", "cost"]
    form = OrderForm


admin.site.register(Order, OrderAdmin)
