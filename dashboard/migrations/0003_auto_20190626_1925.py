# Generated by Django 2.2.2 on 2019-06-26 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190626_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapydserver',
            old_name='mode_name',
            new_name='node_name',
        ),
    ]