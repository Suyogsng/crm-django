from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from crm_app.constants import(
    COMMUNICATION_MEDIUM, CUSTOMER_STATUS, DEAL_STATUS, ACTION_CHOICES,
    PRIORITIES)


class Employee(User):
    designation = models.ForeignKey('Designation', null=True, blank=True)
    mobile_number = models.BigIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    email_address = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    spokesmen = models.BooleanField(default=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.BigIntegerField(null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    interested_product = models.ManyToManyField(Product)
    previous_deals = models.ManyToManyField('Deal', related_name='previous_deals', null=True, blank=True )
    reply_deadline = models.DateTimeField()
    contact_person = models.ForeignKey(Employee)
    contact_date = models.DateTimeField(null=True, blank=True)
    communicate_through = models.CharField(max_length=20, choices=COMMUNICATION_MEDIUM)
    status = models.CharField(max_length=10, choices=CUSTOMER_STATUS)

    def __str__(self):
        return self.name


class Deal(models.Model):
    title = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=DEAL_STATUS)
    product = models.ManyToManyField(Product)
    description = models.TextField(null=True, blank=True)
    advance = models.PositiveIntegerField()
    budget = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Transaction(models.Model):
    deal = models.ForeignKey(Deal)
    date = models.DateTimeField()
    payment_through = models.CharField(max_length=50, null=True, blank=True)
    tax_rate = models.IntegerField(null=True, blank=True)
    discount_rate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.deal.title


class Messaging(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer)
    urgency = models.CharField(max_length=20, choices=PRIORITIES)
    body = models.TextField()

    def __str__(self):
        return self.subject


class Feeds(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    deal = models.ForeignKey(Deal, null=True, blank=True)
    # type

    def __str__(self):
        return self.employee.username

class Comment(models.Model):
    employee = models.ForeignKey(Employee)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    feed = models.ForeignKey(Feeds)

    def __str__(self):
        return self.employee.username


class ProjectLog(models.Model):
    deal = models.ForeignKey(Deal)
    updated_on = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee)

    def __str__(self):
        return self.deal.title


class ActionLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.action_type


class Designation(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
