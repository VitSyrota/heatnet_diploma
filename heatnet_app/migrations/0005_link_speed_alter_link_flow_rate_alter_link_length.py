# Generated by Django 5.0.4 on 2024-04-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heatnet_app', '0004_rename_weight_link_flow_rate_remove_project_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='speed',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='м/с'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='flow_rate',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='т/год'),
        ),
        migrations.AlterField(
            model_name='link',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='м'),
        ),
    ]
