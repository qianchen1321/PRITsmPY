from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(project_orders)
admin.site.register(project_devicelist)
admin.site.register(DeviceToRackInfo)
