from django.contrib import admin
from .models import (Product, ProductGroup, MeasurementUnit,
                     ReceiveInvoice, ReceiveInvoiceOrder,
                     LeaveInvoice, LeaveInvoiceOrder, Storage)

admin.site.register(Product)
admin.site.register(ProductGroup)
admin.site.register(MeasurementUnit)
admin.site.register(Storage)
admin.site.register(ReceiveInvoice)
admin.site.register(ReceiveInvoiceOrder)
admin.site.register(LeaveInvoice)
admin.site.register(LeaveInvoiceOrder)
