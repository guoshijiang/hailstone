# Generated by Django 2.2.3 on 2022-10-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20221003_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='symbol',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='symbol/%Y/%m/%d/'),
        ),
    ]
