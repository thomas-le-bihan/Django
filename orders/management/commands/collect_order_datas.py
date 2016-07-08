from django.core.management.base import BaseCommand
from django.http.response import HttpResponseBadRequest

from orders.models import Order
try:
    from xml.etree import cElementTree as ElementTree
except ImportError, e:
    from xml.etree import ElementTree
import requests


class Command(BaseCommand):
    """
    Command that collect orders datas
    """

    def handle(self, *args, **options):
        # Get xml
        response = requests.get('http://test.lengow.io/orders-test.xml')
        if response.status_code != 200:
            return HttpResponseBadRequest('Error: GET http://test.lengow.io/orders-test.xml')

        xml = response.content

        # Browse and parse xml
        tree = ElementTree.fromstring(xml)
        for elem in tree.iter('order'):
            # Create order and save it
            order = Order(
                order_id=elem.find('order_id').text,
                order_mrid=elem.find('order_mrid').text,
                order_refid=elem.find('order_refid').text,
                order_amount=elem.find('order_amount').text,
                marketplace=elem.find('marketplace').text)
            order.save()
