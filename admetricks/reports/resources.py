from tastypie.resources import ModelResource
from models import Campaign

class CampaignResource(ModelResource):
    class Meta:
        queryset = Campaign.objects.all()
        resource_name = 'campaign'
        allowed_methods = ['get']
