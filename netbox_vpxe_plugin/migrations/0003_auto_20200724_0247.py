# Generated by Django 3.0.8 on 2020-07-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_vpxe_plugin', '0002_auto_20200723_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootconfig',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bootconfig',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='bootimage',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bootimage',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='bootprofile',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='bootprofile',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]