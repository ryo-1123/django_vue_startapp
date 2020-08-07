"""
支払い情報
"""
from django.db import models
from payments.models.payment import Payment
from items.models.items import Item

class PaymentRole(models.Model):
    pay_id = models.ForeignKey(Payment, verbose_name='支払い情報ID', db_column='pay_id', on_delete=models.PROTECT)
    item_id = models.ForeignKey(Item, verbose_name='商品ID', db_column='item_id', on_delete=models.PROTECT)
    item_q = models.IntegerField(verbose_name='購入数')


    class Meta:
        db_table='payment_role'

        verbose_name='支払い情報ロール'

        verbose_name_plural='payment_role'
