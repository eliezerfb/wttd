from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only acept digits"""
        form = self.make_validate_form(cpf='ABC12345898')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validate_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalize(self):
        """Name must be capitalize"""
        form = self.make_validate_form(name='ELIÉZER bourchardt')
        self.assertEqual('Eliézer Bourchardt', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """E-mail is optional"""
        form = self.make_validate_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validate_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email and phone are optional, but one must be informed"""
        form = self.make_validate_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def test_without_phone_and_invalid_email(self):
        """Email and phone are optional, but one must be informed"""
        form = self.make_validate_form(email='xpto', phone='')
        self.assertListEqual(sorted(['__all__', 'email']),
                             sorted(list(form.errors)))

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def make_validate_form(self, **kwargs):
        valid = dict(name='Eliézer Bourchardt', cpf='12345678901',
                     email='eliezerfb@gmail.com', phone='49-9-84020730')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form


class TemplateRegressionTest(TestCase):
    def test_template_has_non_fields_errors(self):
        invalid_data = dict(name="Eliézer Bourchardt", cpf="12345678901")
        response = self.client.post(r('subscriptions:new'), invalid_data)

        self.assertContains(response, '<ul class="errorlist nonfield">')
