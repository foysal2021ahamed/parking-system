# Generated by Django 3.1.7 on 2021-04-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contactno', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('address', models.CharField(default='', max_length=200)),
                ('space', models.CharField(default='', max_length=30)),
                ('message', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mail', models.CharField(default='null', max_length=200)),
                ('contactno', models.CharField(default='', max_length=10)),
                ('question', models.CharField(default='', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicleentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vnumber', models.CharField(max_length=10)),
                ('vtype', models.CharField(choices=[('two', 'Two Wheeler'), ('three', 'Three Wheeler'), ('four', 'Four Wheeler')], default='two', max_length=10)),
                ('contactno', models.CharField(default='', max_length=10)),
                ('date', models.DateField(blank=True, null=True)),
                ('intime', models.TimeField(blank=True, null=True)),
                ('spacealloted', models.CharField(max_length=10)),
                ('flooralloted', models.CharField(max_length=10)),
                ('tagno', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicleexit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vno', models.CharField(default='', max_length=10)),
                ('vty', models.CharField(choices=[('two', 'Two Wheeler'), ('three', 'Three Wheeler'), ('four', 'Four Wheeler')], default='two', max_length=10)),
                ('outtime', models.TimeField(blank=True, null=True)),
                ('farem', models.CharField(blank=True, max_length=4, null=True)),
                ('tno', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
