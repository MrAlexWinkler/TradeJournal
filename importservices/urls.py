from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("transactions/", ImportEntriesView.as_view(), name="import"),
]
