# Generated by Django 4.2 on 2023-04-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_alter_packages_options_alter_userpackages_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='status_change_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
