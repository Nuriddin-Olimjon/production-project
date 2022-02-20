# Generated by Django 4.0.2 on 2022-02-20 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_leaveinvoiceorder_receiveinvoiceorder_and_more'),
        ('finance', '0003_cashbox_cashier'),
        ('user', '0002_user_currency_user_storage_alter_user_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='storage',
        ),
        migrations.AddField(
            model_name='user',
            name='storages',
            field=models.ManyToManyField(to='storage.Storage', verbose_name='Omborlar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.currency', verbose_name='Valyuta'),
        ),
    ]