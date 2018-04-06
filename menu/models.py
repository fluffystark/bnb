# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

STATUS_CHOICES = {
    (1, "PENDING"),
    (2, "SERVED"),
    (3, "PAID")
}


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuSubtype(models.Model):
    name = models.CharField(max_length=50)
    is_quantified = models.BooleanField(default=False)
    menutype = models.ForeignKey(MenuType,
                                 related_name='menusubtypes',)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menusubtype = models.ForeignKey(MenuSubtype,
                                    related_name='menuitems',)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(default=100.00)

    def __str__(self):
        return self.name


class Order(models.Model):

    PENDING = 1
    SERVED = 2
    PAID = 3

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    ordernum = models.SmallIntegerField()
    customer = models.ForeignKey(Customer,
                                 related_name='order', null=True)
    total = models.FloatField()

    def __str__(self):
        return self.customer.name + " " + str(self.ordernum)


class OrderItem(models.Model):

    PENDING = 1
    SERVED = 2
    PAID = 3

    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    order = models.ForeignKey(Order,
                              related_name='orderitems',)
    menuitem = models.ForeignKey(MenuItem,
                                 related_name='orderitems',)
    price = models.FloatField()

    def __str__(self):
        return str(self.order.ordernum) + " " + self.menuitem.name

    def status_color(self):
        color = "bg-warning"
        if self.status == self.SERVED:
            color = "bg-secondary"
        elif self.status == self.PAID:
            color = "bg-success"
        return color
