from django.contrib import admin
from .models import (Product, ProductGroup, MeasurementUnit,
                     ReceiveInvoice, Storage, LeaveInvoice)

admin.site.register(Product)
admin.site.register(ProductGroup)
admin.site.register(MeasurementUnit)
admin.site.register(Storage)
admin.site.register(ReceiveInvoice)
admin.site.register(LeaveInvoice)
