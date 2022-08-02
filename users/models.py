from decimal        import Decimal
from django.db      import models

from core.models    import TimeStampModel

class User(TimeStampModel):
    first_name          = models.CharField(max_length = 50)
    last_name           = models.CharField(max_length = 50)
    email               = models.CharField(max_length = 50)
    kakao_id            = models.BigIntegerField(unique=True)
    kakao_profile_img   = models.CharField(max_length = 500)
    phone_number        = models.CharField(max_length = 50)
    birth_day           = models.CharField(max_length = 50)
    point               = models.DecimalField(max_digits = 10, decimal_places = 2, default=Decimal('100000.00'))
        
    class Meta:
        db_table = 'users'