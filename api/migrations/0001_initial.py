# Generated by Django 3.1.3 on 2020-12-09 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('VNNo', models.CharField(db_column='VNNo', max_length=17, primary_key=True, serialize=False)),
                ('CarMaker', models.CharField(db_column='CarMaker', max_length=15)),
                ('CarModel', models.CharField(db_column='CarModel', max_length=10)),
                ('Year', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustID', models.CharField(db_column='CustID', max_length=100, primary_key=True, serialize=False)),
                ('CustName', models.CharField(db_column='CustName', max_length=100)),
                ('CustPhone', models.CharField(db_column='CustPhone', max_length=100)),
                ('CustAddress', models.TextField(db_column='CustAddress', max_length=100)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.CharField(db_column='EmployeeID', max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(db_column='Name', max_length=15)),
                ('Phone', models.CharField(db_column='Phone', max_length=10)),
                ('Address', models.TextField(db_column='Address', max_length=30)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='ThreeMFilm',
            fields=[
                ('ThreeMFilmType', models.CharField(db_column='ThreeMFilmType', max_length=20, primary_key=True, serialize=False)),
                ('Size', models.IntegerField(db_column='Size')),
                ('Markup', models.IntegerField(db_column='Markup')),
                ('QuantityRemain', models.IntegerField(db_column='QuantityRemain', default=0)),
            ],
            options={
                'db_table': 'threemfilm',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('Service_Type', models.CharField(db_column='Service_Type', max_length=20, primary_key=True, serialize=False)),
                ('Service_Price', models.IntegerField(db_column='Service_Price', default=0)),
                ('ThreeMFilmType', models.ForeignKey(db_column='ThreeMFilmType', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.threemfilm')),
            ],
            options={
                'db_table': 'service',
                'unique_together': {('Service_Type', 'Service_Price')},
            },
        ),
        migrations.CreateModel(
            name='Req',
            fields=[
                ('RequestID', models.CharField(db_column='RequestID', max_length=10, primary_key=True, serialize=False)),
                ('Roll_size', models.IntegerField(db_column='Roll_size')),
                ('Quantity', models.IntegerField(db_column='Quantity')),
                ('Date', models.DateField(db_column='Date')),
                ('EmpID', models.ForeignKey(db_column='EmpID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.employee')),
            ],
            options={
                'db_table': 'requests',
            },
        ),
        migrations.CreateModel(
            name='RepairOrder',
            fields=[
                ('RONumber', models.CharField(db_column='RONumber', max_length=8, primary_key=True, serialize=False)),
                ('Date', models.DateField(db_column='Date')),
                ('HoursWorked', models.IntegerField(db_column='HoursWorked', default=0)),
                ('FilmUsed', models.IntegerField(db_column='FilmUsed', default=0)),
                ('CustID', models.ForeignKey(db_column='CustID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.customer')),
                ('EmployeeID', models.ForeignKey(db_column='EmployeeID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.employee')),
                ('ServiceType', models.ForeignKey(db_column='ServiceType', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.service')),
                ('VNNo', models.ForeignKey(db_column='VNNo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.car')),
            ],
            options={
                'db_table': 'repairorder',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='CustID',
            field=models.ForeignKey(db_column='CustID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.customer'),
        ),
    ]
