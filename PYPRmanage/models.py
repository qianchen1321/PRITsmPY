from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.

POWERUNIT = 'W'
KPOWERUNIT = 'KW'
power_unit_choice = [
    (POWERUNIT, '瓦'),
    (KPOWERUNIT, '千瓦'),
]


def max_rackvalue_valid(value, fix):
    if value < fix:
        raise ValidationError(
            _('%(value)s 必须小于机柜高度值'),
            params={'value': value}
        )

class project_orders(models.Model):
    HOSTUNIT = "TAI"
    MEMUNIT = 'TIAO'
    BLOCKUIT = 'KUAI'
    SUBASSEMBLE = 'GE'

    unit_choice = [
        (HOSTUNIT,"台"),
        (MEMUNIT, "条"),
        (BLOCKUIT,"块"),
        (SUBASSEMBLE,"个"),
    ]

    #Purchase_OrderId = models.AutoField(primary_key=True)
    Main_type = models.CharField(max_length=20, null=False, unique=True, primary_key=True)
    Business_type = models.CharField(max_length=20, null=False)
    Brand = models.CharField(max_length=10, null=False)
    Device_config = models.CharField(max_length=500, null=False)
    Quantity_require = models.IntegerField(null=False)
    unitType = models.CharField(max_length=5, choices=unit_choice, default=HOSTUNIT)
    Power = models.IntegerField(null=True)
    PowerUnit = models.CharField(max_length=10, choices=power_unit_choice, default=POWERUNIT)

class project_devicelist(models.Model):
    hostname = models.CharField(max_length=50, null=False, unique=True, primary_key=True)
    #Main_type = models.CharField(max_length=20, null=False, unique=True)
    sn = models.CharField(max_length=10, null=False)
    remark1 = models.CharField(max_length=20, null=True)
    remark2 = models.CharField(max_length=20, null=True)
    Main_type = models.ForeignKey(project_orders, on_delete=models.CASCADE)


class RackInfo(models.Model):
    Rackid = models.CharField(max_length=20, unique=True, primary_key=True)
    Power = models.IntegerField(null=True)
    PowerUnit = models.CharField(max_length=4, choices=power_unit_choice, default=POWERUNIT)



class DeviceToRackInfo(models.Model):
    # RackRelateHostId = models.AutoField()
    Rackid = models.CharField(max_length=10, primary_key=True)
    hostname = models.CharField(max_length=50, null=False, default="hostname_lost")
    start_Rackuint =models.DecimalField(max_digits=2, decimal_places=0, null=False, validators=[MaxValueValidator(42, message="the height must below than 42"),
                                                                              MinValueValidator(1, message="the heigt must be at least 1")], default=0)
    end_Rackuint =models.DecimalField(max_digits=2, decimal_places=0, null=False, validators=[MaxValueValidator(42, message="the height must below than 42"),
                                                                              MinValueValidator(1, message="the heigt must be at least 1")], default=0)


