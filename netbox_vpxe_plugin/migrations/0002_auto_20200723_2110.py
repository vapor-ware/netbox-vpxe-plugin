# Generated by Django 3.0.8 on 2020-07-23 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_vpxe_plugin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bootprofile',
            old_name='boot_config',
            new_name='config',
        ),
        migrations.RenameField(
            model_name='bootprofile',
            old_name='boot_image',
            new_name='image',
        ),
    ]
