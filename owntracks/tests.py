import json

from django.test import Client, RequestFactory, TestCase

from accounts.models import BlogUser
from .models import OwnTrackLog


# Create your tests here.

class OwnTrackLogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_own_track_log(self):
        o = {
            'tid': 12,
            'lat': 123.123,
            'lon': 134.341
        }

        self.client.post(
            '/owntracks/logtracks',
            json.dumps(o),
            content_type='application/json')
        length = len(OwnTrackLog.objects.all())
        self.assertEqual(length, 1)

        o = {
            'tid': 12,
            'lat': 123.123
        }

        self.client.post(
            '/owntracks/logtracks',
            json.dumps(o),
            content_type='application/json')
        length = len(OwnTrackLog.objects.all())
        self.assertEqual(length, 1)

        rsp = self.client.get('/owntracks/show_maps')
        self.assertEqual(rsp.status_code, 302)

        user = BlogUser.objects.create_superuser(
            email="juestnow@gmail.com",
            username="juestnow",
            password="juestnow")

        self.client.login(username='juestnow', password='juestnow')
        s = OwnTrackLog()
        s.tid = 12
        s.lon = 123.234
        s.lat = 34.234
        s.save()

        rsp = self.client.get('/owntracks/show_dates')
        self.assertEqual(rsp.status_code, 200)
        rsp = self.client.get('/owntracks/show_maps')
        self.assertEqual(rsp.status_code, 200)
        # rsp = self.client.get('/owntracks/get_datas')
        # self.assertEqual(rsp.status_code, 200)
        # rsp = self.client.get('/owntracks/get_datas?date=2018-02-26')
        # self.assertEqual(rsp.status_code, 200)
