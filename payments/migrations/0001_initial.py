# Generated by Django 3.0.8 on 2020-08-06 00:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pay_id', models.AutoField(primary_key=True, serialize=False)),
                ('pay_total_price', models.IntegerField(verbose_name='合計金額')),
                ('email', models.EmailField(max_length=254, verbose_name='Eメール')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
            ],
            options={
                'verbose_name': '支払い情報',
                'verbose_name_plural': 'payments',
                'db_table': 'payments',
            },
        ),
    ]
