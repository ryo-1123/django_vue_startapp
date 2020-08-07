"""
支払い情報
"""
from django.db import models
from django.utils import timezone

class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    pay_total_price = models.IntegerField(verbose_name='合計金額')
    email = models.EmailField(verbose_name='Eメール')
    created_at = models.DateTimeField(verbose_name='登録日時', default=timezone.now)


    class Meta:
        db_table='payments'

        verbose_name='支払い情報'

        verbose_name_plural='payments'
