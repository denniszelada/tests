from django.db.models import Sum, Count
from tastypie import fields
from models import Campaign, CampaignSummary
from sets import Set
from utils import CampaignResource
import secrets

class ChartResource(CampaignResource):
    label = fields.CharField(attribute='campaign', null=True)
    fillColor = fields.CharField(attribute='fillColor', default='rgba(162, 162, 162, 0.53)')
    strokeColor = fields.CharField(attribute='strokeColor', default="#bebebe")
    pointColor = fields.CharField(attribute='pointColor', default="#bebebe")
    pointStrokeColor = fields.CharField(attribute='pointStrokeColor', default='#bebebe')
    pointHighlightStroke = fields.CharField(attribute='pointHighlightStroke',null=True)
    data = fields.ListField(null=True, attribute='data')

    def __init__(self, api_name=None):
        self.labels = Set()
        self.colors = ['rgba(233, 30, 99, 0.65)', 'rgba(30, 136, 229, 0.65)', 'rgba(38, 166, 154, 0.65)',
        'rgba(255, 87, 34, 0.65)', 'rgba(255, 193, 7, 0.65)', 'rgba(247, 39, 24, 0.65)']
        super(ChartResource, self).__init__(api_name)

    class Meta:
        resource_name = 'chart'
        include_resource_uri = False
        detail_allowed_methods = []

    def obj_get_list(self, bundle, **kwargs):
        object_list = self.get_object_list(bundle, **kwargs)
        # Gets the list of available dates
        dates = object_list.values('date').distinct()
        self.labels = self.wrap_dictionary(dates, 'date')

        #Gets the list of available campaigns
        objects = object_list.values('campaign').distinct()
        objects = self.wrap_data(objects)

        for label in self.labels:
            for obj in objects:
                if not obj['data']:
                    obj['data'] = []

                value = object_list.filter(date=label, campaign=obj['campaign']).aggregate(impact = Sum('impact'))
                obj['data'].append(value['impact'] or 0)
                color = secrets.SystemRandom().choice(self.colors)
                obj['pointHighlightFill'] = color
                obj['pointHighlightStroke'] = color
                obj['strokeColor'] = color
                obj['fillColor'] = color
                obj['pointColor'] = color

        return objects

    def alter_list_data_to_serialize(self, request, data):
        objects = data['objects']
        altered_data = {'labels':self.labels, 'datasets':objects}
        data['objects'] = altered_data
        return data


class MediaResource(CampaignResource):
    media = fields.CharField(attribute='media')
    campaigns = fields.IntegerField(attribute='campaigns')

    class Meta:
        resource_name = 'media'
        detail_allowed_methods = []
        include_resource_uri = False

    """
    Overwritten method
    This allows to get the complete list of campaigns summaries.
    to accomplish the challenge goals
    """
    def obj_get_list(self, bundle, **kwargs):
        object_list = self.get_object_list(bundle, **kwargs)
        object_list = object_list.values('media').annotate(campaigns=Count('campaign'))
        return self.wrap_data(object_list)

class AdvisorsResource(CampaignResource):
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
        object_list = object_list.order_by('-date').values('advisor', 'date','campaign').annotate(impact=Sum('impact'))
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
    Filters and gets the given values with the given objects
    """
    def group_campaign(self,obj, *values):
        return Campaign.objects.filter(campaign=obj.campaign, date=obj.date).values(*values)
