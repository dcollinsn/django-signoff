# -*- coding: utf-8
from django.apps import AppConfig


class SignoffConfig(AppConfig):
    name = 'signoff'

    def ready(self):
        import signoff.signals
