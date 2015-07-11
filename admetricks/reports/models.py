from django.db import models

class Campaign(models.Model):
    """
    Campaign
    --------------------
    This class allows access to data stored under the 'test' table.

    """

    date = models.DateField(db_column='fecha')
    advisor = models.CharField(max_length=255, db_column='avisador')
    campaign = models.CharField(max_length=255, db_column='campanya')
    media = models.CharField(max_length=255, db_column='medio')
    impact = models.IntegerField(db_column='impacto')
    banner = models.URLField(max_length=255)
    class Meta:
        db_table = 'test'
