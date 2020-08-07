# Generated by Django 3.0.8 on 2020-08-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=25, verbose_name='お店の名前')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Eメール')),
                ('password', models.CharField(max_length=30, verbose_name='パスワード')),
                ('withdrawal_datetime', models.DateTimeField(null=True, verbose_name='退会日時')),
            ],
            options={
                'verbose_name': 'お店',
                'verbose_name_plural': 'stores',
                'db_table': 'store',
            },
        ),
    ]
