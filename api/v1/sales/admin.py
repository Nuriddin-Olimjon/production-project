from django.contrib import admin
from .models import Client, ClientBankDetail, City


admin.site.register(Client)
admin.site.register(ClientBankDetail)
admin.site.register(City)

