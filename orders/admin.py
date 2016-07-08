from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_mrid', 'order_refid',
                    'order_amount', 'marketplace')
    search_fields = ('order_id', 'order_mrid', 'order_refid',
                     'order_amount', 'marketplace')
admin.site.register(Order, OrderAdmin)
