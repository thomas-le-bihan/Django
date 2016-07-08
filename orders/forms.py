from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('id', 'order_id', 'order_mrid',
                  'order_refid', 'order_amount',
                  'marketplace')
