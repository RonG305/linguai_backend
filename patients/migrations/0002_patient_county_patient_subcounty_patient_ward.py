# Generated by Django 5.1.1 on 2024-10-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='county',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='subcounty',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='ward',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]