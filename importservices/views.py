import importlib
from typing import Any, Dict

from django.db.models import Q
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from .models import *


class ImportEntriesView(TemplateView):

    template_name = "importservices/import_transactions.html"
