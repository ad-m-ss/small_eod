# Generated by Django 3.1.1 on 2020-10-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0012_auto_20200527_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='comment',
            field=models.TextField(blank=True, help_text='Comment for this case.', verbose_name='Comment'),
        ),
    ]
