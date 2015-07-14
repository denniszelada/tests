#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from models import Campaign
from tastypie.test import ResourceTestCase


class CampaignResourceTest(ResourceTestCase):
    fixtures = ['test-campaigns.json']

    def setUp(self):
        super(CampaignResourceTest, self).setUp()

        self.campaign = Campaign.objects.get(id=1)

        self.detail_url = '/api/v1/campaigns/{0}/'.format(self.campaign.pk)

    """
    Verifica el acceso al recurso de campaña sin un header de autorización
    """
    def test_get_list_unauthorized(self):
        resp = self.api_client.get('/api/v1/campaigns/')
        self.assertHttpOK(resp)

    """
    Verifica que la respuesta del servidor sea un 405 en los métodos no permitidos,
    post, put, delete
    """
    def test_not_allowed_methods(self):
        data = {'data':'empty data or anything'}
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.post('/api/v1/campaigns/',data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.put(self.detail_url ,data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.delete(self.detail_url)
        self.assertHttpMethodNotAllowed(resp)

    """
    Obtiene la primera página de recursos y la
    """
    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/campaigns/', format='json')
        self.assertValidJSONResponse(resp)

        object_list = self.deserialize(resp)
        self.assertEqual(len(object_list['objects']), 20)
        self.assertEqual(len(object_list),2)
        self.assertKeys(object_list['objects'][0],['impact', 'campaign','media','advisor','date','banners'])


class AdvisorsResourceTest(ResourceTestCase):
    fixtures = ['test-campaigns.json']

    def setUp(self):
        super(AdvisorsResourceTest, self).setUp()

        self.campaign = Campaign.objects.get(id=1)

        self.detail_url = '/api/v1/advisors/{0}/'.format(self.campaign.advisor)

    """
    Verifica el acceso al recurso de campaña sin un header de autorización
    """
    def test_get_list_unauthorized(self):
        resp = self.api_client.get('/api/v1/advisors/')
        self.assertHttpOK(resp)

    """
    Verifica que la respuesta del servidor sea un 405 en los métodos no permitidos,
    post, put, delete
    """
    def test_not_allowed_methods(self):
        data = {'data':'empty data or anything'}
        resp = self.api_client.post('/api/v1/campaigns/',data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.put(self.detail_url ,data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.delete(self.detail_url)
        self.assertHttpMethodNotAllowed(resp)

    """
    Verifica que la respuesta del servidor sea un 405 en los métodos no permitidos,
    post, put, delete
    """
    def test_not_allowed_methods(self):
        data = {'data':'empty data or anything'}
        resp = self.api_client.post('/api/v1/advisors/',data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.put(self.detail_url ,data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.delete(self.detail_url)
        self.assertHttpMethodNotAllowed(resp)

    """
    Obtiene la primera página de recursos y la
    """
    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/advisors/', format='json')
        self.assertValidJSONResponse(resp)

        object_list = self.deserialize(resp)
        self.assertEqual(len(object_list['objects']), 12)
        self.assertEqual(len(object_list),2)
        self.assertKeys(object_list['objects'][0],['advisor', 'campaigns'])

class MediaResourceTest(ResourceTestCase):
    fixtures = ['test-campaigns.json']

    def setUp(self):
        super(MediaResourceTest, self).setUp()

        self.campaign = Campaign.objects.get(id=1)

        self.detail_url = '/api/v1/media/{0}/'.format(self.campaign.advisor)

    """
    Verifica el acceso al recurso de campaña sin un header de autorización
    """
    def test_get_list_unauthorized(self):
        resp = self.api_client.get('/api/v1/media/')
        self.assertHttpOK(resp)

    """
    Verifica que la respuesta del servidor sea un 405 en los métodos no permitidos,
    post, put, delete
    """
    def test_not_allowed_methods(self):
        data = {'data':'empty data or anything'}
        resp = self.api_client.post('/api/v1/media/',data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.put(self.detail_url ,data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.delete(self.detail_url)
        self.assertHttpMethodNotAllowed(resp)

    """
    Obtiene la primera página de recursos y la
    """
    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/media/', format='json')
        self.assertValidJSONResponse(resp)

        object_list = self.deserialize(resp)
        self.assertEqual(len(object_list['objects']), 20)
        self.assertEqual(len(object_list),2)
        self.assertKeys(object_list['objects'][0],['media', 'campaigns'])

class ChartResourceTest(ResourceTestCase):
    fixtures = ['test-campaigns.json']

    def setUp(self):
        super(ChartResourceTest, self).setUp()

        self.campaign = Campaign.objects.get(id=1)

        self.detail_url = '/api/v1/chart/{0}/'.format(self.campaign.advisor)

    """
    Verifica el acceso al recurso de campaña sin un header de autorización
    """
    def test_get_list_unauthorized(self):
        resp = self.api_client.get('/api/v1/chart/')
        self.assertHttpOK(resp)

    """
    Verifica que la respuesta del servidor sea un 405 en los métodos no permitidos,
    post, put, delete
    """
    def test_not_allowed_methods(self):
        data = {'data':'empty data or anything'}
        resp = self.api_client.post('/api/v1/chart/',data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.put(self.detail_url ,data=data)
        self.assertHttpMethodNotAllowed(resp)

        resp = self.api_client.delete(self.detail_url)
        self.assertHttpMethodNotAllowed(resp)

    """
    Obtiene la primera página de recursos
    """
    def test_get_list_json(self):
        resp = self.api_client.get('/api/v1/chart/', format='json')
        self.assertValidJSONResponse(resp)

        object_list = self.deserialize(resp)
        self.assertEqual(len(object_list['objects']), 2)
        self.assertEqual(len(object_list),2)
        self.assertKeys(object_list['objects'],['datasets', 'labels'])
        self.assertKeys(object_list['objects']['datasets'][0],
                    ['data','fillColor','label','pointColor',
                       'pointHighlightStroke', 'pointStrokeColor','strokeColor'])
