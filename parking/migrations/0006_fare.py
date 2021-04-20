# Generated by Django 3.1.7 on 2021-04-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0005_plots_plot_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_hour_fare', models.PositiveIntegerField(default=0)),
                ('plot_type', models.CharField(choices=[('two', 'Two Wheeler'), ('three', 'Three Wheeler'), ('four', 'Four Wheeler')], default='four', max_length=10)),
            ],
        ),
    ]