# Generated by Django 2.0.4 on 2018-05-28 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Exchange Name')),
                ('url', models.CharField(max_length=100, unique=True, verbose_name='Exchange URL')),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.CharField(max_length=100, unique=True, verbose_name='Exchange Api')),
                ('coin_change', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_coin_change', to='coins.CoinChange')),
                ('exchange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_exchange', to='exchanges.Exchange')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100, verbose_name='Value')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('exchange_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_exchange_coin', to='exchanges.ExchangeCoin')),
            ],
        ),
    ]
