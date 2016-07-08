from rest_framework import serializers, viewsets
from orders.models import Order


# Serializers define the API representation.
class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ('order_id', 'order_mrid', 'order_refid',
                  'order_amount', 'marketplace')


# ViewSets define the view behavior.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get']
