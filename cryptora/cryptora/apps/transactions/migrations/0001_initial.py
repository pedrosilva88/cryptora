# Generated by Django 2.0.4 on 2018-05-30 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchanges', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_token', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Price per token')),
                ('n_tokens', models.DecimalField(decimal_places=8, max_digits=20, verbose_name='tokens')),
                ('fees', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='fees')),
                ('date', models.DateTimeField(verbose_name='Transaction Date')),
                ('sync', models.BooleanField(default=False, verbose_name='Synced Transaction')),
                ('exchange_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_exchange_coin', to='exchanges.ExchangeCoin')),
                ('synced_transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction_synced', to='transactions.Transaction')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='TransactionMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], default='BUY', max_length=20, verbose_name='Transaction type')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_transaction_method', to='transactions.TransactionMethod'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_user', to=settings.AUTH_USER_MODEL),
        ),
    ]