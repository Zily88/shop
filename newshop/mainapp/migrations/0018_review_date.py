# Generated by Django 2.1 on 2018-09-23 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20180923_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
