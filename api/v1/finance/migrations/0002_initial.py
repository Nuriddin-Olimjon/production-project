# Generated by Django 4.0.2 on 2022-02-19 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kassir'),
        ),
        migrations.AddField(
            model_name='payment',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.currency', verbose_name='Valyuta'),
        ),
        migrations.AddField(
            model_name='payment',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to=settings.AUTH_USER_MODEL, verbose_name='Hodim'),
        ),
        migrations.AddField(
            model_name='payment',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier', verbose_name="Ta'minotchi"),
        ),
        migrations.AddField(
            model_name='income',
            name='cashbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.cashbox', verbose_name='Kassa nomi'),
        ),
        migrations.AddField(
            model_name='income',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.client', verbose_name='Mijoz'),
        ),
        migrations.AddField(
            model_name='income',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kassir'),
        ),
        migrations.AddField(
            model_name='income',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.currency', verbose_name='Valyuta'),
        ),
        migrations.AlterUniqueTogether(
            name='subcosttype',
            unique_together={('type', 'title')},
        ),
    ]