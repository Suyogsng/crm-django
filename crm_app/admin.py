from django.contrib import admin
from .models import (
    Employee, Customer, Deal, Transaction, Comment, Feeds, Product,
    Messaging, ProjectLog, ActionLog, Designation)

admin.site.register([
    Employee, Customer, Deal, Transaction, Comment, Feeds, Product,
    Messaging, ProjectLog, ActionLog, Designation])
