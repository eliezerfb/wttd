from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Eliézer Bourchardt', cpf='12345678910',
                    email='eliezerfb@gmail.com', phone='49-98402-0730')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'eliezerfb@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Eliézer Bourchardt',
            '12345678910',
            'eliezerfb@gmail.com',
            '49-98402-0730',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
