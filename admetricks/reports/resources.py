from django.db.models import Sum, Count
from tastypie import fields
from models import Campaign, CampaignSummary
from sets import Set
from utils import CampaignResource

class AdvisorsRecource(CampaignResource):
    advisor = fields.CharField(attribute='advisor')
    campaigns = fields.IntegerField(attribute='campaigns')

    class Meta:
        resource_name = 'advisors'
        detail_allowed_methods = []
        include_resource_uri = False
    """
    Overwritten method
    This allows to get the complete list of campaigns summaries.
    to accomplish the challenge goals
    """
    def obj_get_list(self, bundle, **kwargs):
        object_list = self.get_object_list(bundle, **kwargs)
        object_list = object_list.values('advisor').annotate(campaigns=Count('campaign'))
        return self.wrap_data(object_list)
    
class CampaignSummaryResource(CampaignResource):
    advisor = fields.CharField(attribute='advisor')
    campaign = fields.CharField(attribute='campaign')
    impact = fields.IntegerField(attribute='impact')
    date = fields.DateField(attribute='date')
    media = fields.ListField()
    banners = fields.ListField()

    class Meta:
        resource_name = 'campaigns'
        detail_allowed_methods = []
        include_resource_uri = False

        
    """
    Overwritten method
    This allows to get the complete list of campaigns summaries.
    to accomplish the challenge goals
    """
    def obj_get_list(self, bundle, **kwargs):
        object_list = self.get_object_list(bundle, **kwargs)
        object_list = object_list.values('advisor', 'date','campaign').annotate(impact=Sum('impact'))
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
    Converts a list of dictionaries into a list, by
    searching the key given
    """
    def wrap_dictionary(self, data, key):
        wrapped = Set()
        results = []
        for (k,v) in enumerate(data):
            result = v[key]
            if not result in wrapped:
                results.append(v[key])
                wrapped.add(result)
        return results

    """
    Filters and gets the given values with the given objects
    """
    def group_campaign(self,obj, *values):
        return Campaign.objects.filter(campaign=obj.campaign, date=obj.date).values(*values)
