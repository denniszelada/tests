from django.db import models

class CampaignSumarry(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data

class Campaign(models.Model):
    """
    Campaign
    --------------------
    This class allows access to data stored under the 'test' table.

    """

    date = models.DateField(db_column='fecha')
    advisor = models.CharField(max_length=255, db_column='avisador', null=True)
    campaign = models.CharField(max_length=255, db_column='campanya', null=True)
    media = models.CharField(max_length=255, db_column='medio', null=True)
    impact = models.IntegerField(db_column='impacto', null=True)
    banner = models.URLField(max_length=255, null=True)
    class Meta:
        db_table = 'test'
