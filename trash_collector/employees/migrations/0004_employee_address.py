# Generated by Django 3.2.8 on 2021-11-03 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_rename_employeeinfo_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
