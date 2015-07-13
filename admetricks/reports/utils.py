from tastypie.resources import Resource
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpMethodNotAllowed
from models import Campaign, CampaignSummary

class CampaignResource(Resource):
    class Meta:
        allowed_methods = ['get']

    def obj_get(self, bundle, **kwargs):
        raise ImmediateHttpResponse(HttpMethodNotAllowed('Sorry you can\'t do that'))

    def obj_create(self, bundle, **kwargs):
        raise ImmediateHttpResponse(HttpMethodNotAllowed('Sorry you can\'t do that'))

    def obj_delete(self, bundle, **kwargs):
        raise ImmediateHttpResponse(HttpMethodNotAllowed('Sorry you can\'t do that'))

    def obj_delete_list(self, bundle, **kwargs):
        raise ImmediateHttpResponse(HttpMethodNotAllowed('Sorry you can\'t do that'))
    """
    Overwritten method
    Builds allowed filters
    """
    def get_object_list(self, bundle, **kwargs):
        import datetime
        params = bundle.request.GET
        objects = Campaign.objects
        if 'date' in params:
            date = datetime.datetime.strptime(params['date'], '%d%m%Y').date()
            objects = objects.filter(date= str(date))
        return objects

    """
    Converts a group of flat data into serializable objects
    """
    def wrap_data(self, data=[]):
        results = []
        for result in data:
            new_obj = CampaignSummary(initial=result)
            results.append(new_obj)
        return results
