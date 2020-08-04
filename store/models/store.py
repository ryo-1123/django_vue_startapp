"""
お店テーブル
"""
from django.db import models
from django.utils import timezone

class Store(models.Model):
    """
    お店 テーブルのモデルクラス
    """
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(verbose_name='お店の名前', max_length=25)
    email = models.EmailField(verbose_name='Eメール', unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=30)
    withdrawal_datetime = models.DateTimeField(verbose_name='退会日時', null=True)

    class Meta:
        db_table='store'

        verbose_name='お店'

        verbose_name_plural='stores'
