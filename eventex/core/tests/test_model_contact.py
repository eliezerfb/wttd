from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Eliézer Bourchardt',
            slug='eliezer-bourchardt',
            photo='https://avatars3.githubusercontent.com/u/25516007?s=460&v=4'
        )


    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,
            kind=Contact.EMAIL,
            value='eliezerfb@gmail.com'
        )
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,
            kind=Contact.PHONE,
            value='49-9-8402-0730'
        )
        self.assertTrue(Contact.objects.exists())

    def test_choiches(self):
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker,
            kind=Contact.EMAIL,
            value='eliezerfb@gmail.com'
        )
        self.assertEqual('eliezerfb@gmail.com', str(contact))
