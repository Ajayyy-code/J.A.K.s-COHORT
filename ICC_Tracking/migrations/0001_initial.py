# Generated by Django 3.2.9 on 2021-11-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bearer',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('assignedOrders', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('orderID', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('company', models.CharField(default='N/A', max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('optionalAddressInfo', models.CharField(default='N/A', max_length=50)),
                ('city', models.CharField(default='Portmore', max_length=50)),
                ('country', models.CharField(default='Jamaica', max_length=50)),
                ('contactNumber', models.CharField(max_length=50)),
                ('contactEmail', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('assignedCustomer', models.IntegerField()),
                ('assignedBearer', models.IntegerField()),
                ('subtotal', models.FloatField(max_length=30)),
                ('orderStatus', models.CharField(choices=[(1, 'Pending'), (2, 'Active'), (3, 'Delivered')], default=1, max_length=30)),
            ],
        ),
    ]