"""
商品テーブル
"""
from django.db import models
from django.utils import timezone
from store.models import Store

class Item(models.Model):
    """
    商品 テーブルクラス
    """
    item_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(Store, db_column='store_id', verbose_name='お店ID', on_delete=models.PROTECT)
    item_name = models.CharField(verbose_name='商品名', max_length=30)
    item_img = models.ImageField(upload_to='images', null=True, blank=True)
    item_detail = models.TextField(verbose_name='商品説明', max_length=1000, null=True, blank=True)
    item_price = models.IntegerField(verbose_name='値段')
    item_total = models.IntegerField(verbose_name='在庫')
    created_at = models.DateTimeField(verbose_name='登録日時', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='更新日時', null=True, blank=True, auto_now=True)

    class Meta:
        db_table = 'items'

        verbose_name = '商品'

        verbose_name_plural = 'items'
