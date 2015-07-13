from tastypie.resources import Resource
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpMethodNotAllowed
from models import Campaign, CampaignSummary
from sets import Set

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
            date = datetime.datetime.strptime(params['date'], '%d-%m-%Y').date()
            objects = objects.filter(date= str(date))
        if 'advisor' in params:
            objects = objects.filter(advisor= params['advisor'])
        if 'media' in params:
            objects = objects.filter(media=params['media'])
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

    """
    Converts a list of dictionaries into a list, by
    searching the key given
    """
    def wrap_dictionary(self, data, key):
        wrapped =  Set()
        results = []
        for (k,v) in enumerate(data):
            result = v[key]
            if not result in wrapped:
                results.append(v[key])
                wrapped.add(result)
        return results
