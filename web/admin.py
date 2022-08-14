from django.contrib import admin
from web.models import Expense,Income
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Expense)
admin.site.register(Income)
