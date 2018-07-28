from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url as r
from django.template.loader import render_to_string
from django.views.generic import DetailView, View, CreateView
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.mixins import EmailCreateView
from eventex.subscriptions.models import Subscription


new = EmailCreateView.as_view(model=Subscription,
                              form_class=SubscriptionForm,
                              email_subject = 'Confirmação de inscrição')

detail = DetailView.as_view(model=Subscription)
