from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription
import uuid

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Eliézer Bourchardt',
            cpf='12345678901',
            email='eliezerfb@gmail.com',
            phone='49984020730'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_create_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Eliézer Bourchardt', str(self.obj))
