# report_builder/apps.py
# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReportBuilderConfig(AppConfig):
    name = 'report_builder'
    label = 'report_builder'
    verbose_name = _("Report Builder")
