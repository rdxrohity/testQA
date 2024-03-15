from django.db import models

class SampleData(models.Model):

    guid = models.CharField(max_length=100)
    geo_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    geo_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date_y_m_d = models.DateField()
    numeric_00 = models.FloatField()
    numeric_01 = models.FloatField()

