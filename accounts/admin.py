from django.contrib import admin
from .models import *


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount', 'date', 'user')


admin.site.register(Expense, ExpenseAdmin)
