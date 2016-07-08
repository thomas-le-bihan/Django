from django.db import models


class Order(models.Model):
    order_id = models.CharField(max_length=100)
    order_mrid = models.CharField(max_length=100)
    order_refid = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=100)
    marketplace = models.CharField(max_length=100)

    def __str__(self):
        return '<Order: %s - %s - %s - %s - %s>'\
                % (self.order_id, self.order_mrid,
                   self.order_refid, self.order_amount,
                   self.marketplace)
