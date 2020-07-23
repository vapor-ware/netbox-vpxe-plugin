# Generated by Django 3.0.8 on 2020-07-23 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BootConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('config', models.TextField()),
                ('type', models.CharField(default='preseed', max_length=30)),
            ],
            options={
                'verbose_name': 'Boot Config',
                'verbose_name_plural': 'Boot Configs',
            },
        ),
        migrations.CreateModel(
            name='BootImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('url', models.URLField()),
                ('family', models.CharField(default='other', max_length=30)),
            ],
            options={
                'verbose_name': 'Boot Image',
                'verbose_name_plural': 'Boot Images',
            },
        ),
        migrations.CreateModel(
            name='BootProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('boot_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netbox_vpxe_plugin.BootConfig')),
                ('boot_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netbox_vpxe_plugin.BootImage')),
            ],
            options={
                'verbose_name': 'Boot Profile',
                'verbose_name_plural': 'Boot Profiles',
            },
        ),
    ]
