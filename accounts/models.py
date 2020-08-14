from django.db import models
from django.contrib.auth.models import User


ExpenseTypes = (('Housing', 'Housing'),
                ('Groceries', 'Groceries'),
                ('Gas', 'Gas'),
                ('Self care', 'Self care'),
                ('Leisure', 'Leisure'),
                ('Debts', 'Debts'),
                ('Utility', 'Utility'),
                ('Gifts', 'Gifts'),
                ('Car care', 'Car care'),
                ('Donations', 'Donations'))


class Expense(models.Model):
    type = models.CharField(max_length=10, choices=ExpenseTypes, default=ExpenseTypes[0])
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

