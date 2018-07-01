from django.test import TestCase
from django.shortcuts import resolve_url as r
import uuid

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Eliézer Bourchardt',
            cpf='12345678901',
            email='eliezerfb@gmail.com',
            phone='49-984020730')
        self.resp = self.client.get(r('subscriptions:detail',
                                      self.obj.hash_id))
#        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.hash_id))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf,
                    self.obj.email, self.obj.phone)
        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', uuid.uuid4()))
        self.assertEqual(404, resp.status_code)
