# Generated by Django 2.0.5 on 2018-07-02 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20180630_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
