from tastypie.resources import Resource
from django.db.models import Sum
from tastypie import fields
from models import Campaign, CampaignSummary

class CampaignSummaryResource(Resource):
    advisor = fields.CharField(attribute='advisor')
    campaign = fields.CharField(attribute='campaign')
    date = fields.DateField(attribute='date')
    impact = fields.IntegerField(attribute='impact')
    media = fields.ListField()
    banners = fields.ListField()
    
    class Meta:
        resource_name = 'campaign'
        allowed_methods = ['get']

    """
    Overwritten method
    This allows to get the complete list of campaigns summaries.
    to accomplish the challenge goals
    """
    def obj_get_list(self, bundle, **kwargs):
        object_list = Campaign.objects.values('advisor', 'campaign', 'date').annotate(impact=Sum('impact'))
        return self.wrap_data(object_list)

    """
    Gets a list of media where the campaign was released
    """
    def dehydrate_media(self, bundle):
        media = self.group_campaign(bundle.obj, 'media')
        return self.wrap_dictionary(media, 'media')

     """
    Gets a list of banners, which are part of the campaign
    """
    def dehydrate_banners(self, bundle):
        banners = self.group_campaign(bundle.obj,'banner')
        return self.wrap_dictionary(banners, 'banner')

    """
    Converts a group of flat data into serializable objects
    """
    def wrap_data(self, data=[]):
        results = []
        for result in data:
            new_obj = CampaignSummary(initial=result)
            results.append(new_obj)
        return results

    """
    Converts a list of dictionaries into a list, by
    searching the key given
    """
    def wrap_dictionary(self, data, key):
        results =  []
        for (k,v) in enumerate(data):
            results.append(v[key])
        return results

    """
    Filters and gets the given values with the given objects
    """
    def group_campaign(self,obj, *values):
        return Campaign.objects.filter(campaign=obj.campaign, date=obj.date).values(*values)
