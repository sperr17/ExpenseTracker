# Generated by Django 2.1 on 2020-08-13 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200813_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='type',
            field=models.CharField(choices=[('Housing', 'Housing'), ('Groceries', 'Groceries'), ('Gas', 'Gas'), ('Self care', 'Self care'), ('Leisure', 'Leisure'), ('Debts', 'Debts'), ('Utility', 'Utility'), ('Gifts', 'Gifts'), ('Car care', 'Car care'), ('Donations', 'Donations')], default=('Housing', 'Housing'), max_length=10),
        ),
    ]
