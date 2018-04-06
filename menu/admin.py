# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from menu.models import *
# Register your models here.

admin.site.register(MenuType)
admin.site.register(MenuSubtype)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)