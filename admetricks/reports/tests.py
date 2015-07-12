import datetime
from models import Campaign
from tastypie.test import ResourceTestCase

class CampaignResourceTest(ResourceTestCase):
    fixtures = ['test-campaigns.json']

    def setup(self):
        super(CampaignResourceTest, self).setUp()

        self.campaign = Campaign.objects.get(id=1)

        self.detail_url = '/api/v1/campaign/{0}/'.format(self.campaign.pk)

    """
    Verifica el acceso al recurso de campanya sin un header de autorizacion
    """
    def test_get_list_unauthorized(self):
        resp = self.api_client.get('/api/v1/campaign/')
        self.assertHttpOK(resp)

    """
    Verifica que la respuesta del servidor sea un 405 en los metodos no permitidos, post, put, delete
    """
    def test_not_allowed_methods(self):
        data = {'data':'empty data or anything'}
        resp = self.api_client.post('/api/v1/campaign/',data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.put(self.detail_url ,data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.delete(self.detail_url)
        self.assertHttpMethodNotAllowed(resp)

    """
    Obtiene la primera pagina de recursos
    """
    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/campaign/', format='json')
        self.assertValidJSONResponse(resp)

        object_list = self.deserialize(resp)
        self.assertEqual(len(object_list['objects']), 20)
        self.assertEqual(len(object_list),2)
        self.assertKeys(object_list['objects'][0],['impact', 'campaign','media','advisor','date','banner'])

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)

        response_object = self.deserialize(resp)
        self.assertKeys(response_object, ['impact', 'campaign','media','advisor','date','banner','id','resource_uri'])
        self.assertEqual(response_object['campaign'], 'Autoexperto')
