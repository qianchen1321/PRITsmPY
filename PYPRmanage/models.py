from django.db import models

# Create your models here.

class project_orders(models.Model):
    HOSTUNIT = "TA"
    MEMUNIT = 'TI'
    BLOCKUIT = 'KU'
    SUBASSEMBLE = 'GE'

    unit_choice = [
        (HOSTUNIT,"台"),
        (MEMUNIT, "条"),
        (BLOCKUIT,"块"),
        (SUBASSEMBLE,"个"),
    ]

    POWERUNIT = 'w'
    KPOWERUNIT = 'KW'
    power_unit_choice = [
        (POWERUNIT, '瓦'),
        (KPOWERUNIT, '千瓦'),
    ]

    Main_type = models.CharField(max_length=20, null=False)
    Business_type = models.CharField(max_length=20, null=False)
    Brand = models.CharField(max_length=10, null=False)
    Device_config = models.CharField(max_length=500, null=False)
    Quantity_require = models.IntegerField(null=False)
    unitType = models.CharField(max_length=2, choices=unit_choice, default=HOSTUNIT)
    Power = models.IntegerField(null=True)
    PowerUnit = models.CharField(max_length=2, choices=power_unit_choice, default=POWERUNIT)




