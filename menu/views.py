# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from menu.models import Order
# Create your views here.


class IndexView(generic.ListView):
    template_name = "order/index.html"
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()
