"""
ユーザテーブル
"""
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='Eメール', unique=True)
    password = models.CharField(verbose_name='パスワード', max_length=30)
    withdrawal_datetime = models.DateTimeField(verbose_name='退会日時', null=True)

    class Meta:
        db_table='users'

        verbose_name='ユーザ'

        verbose_name_plural='users'
