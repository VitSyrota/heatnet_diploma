# Generated by Django 5.0.4 on 2024-04-13 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heatnet_app', '0008_remove_link_end_date_remove_link_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='description',
        ),
        migrations.RemoveField(
            model_name='node',
            name='status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
