# Generated by Django 4.2.7 on 2023-12-04 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kintai', '0004_alter_kintaimodel_overtimealert_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kintaimodel',
            old_name='paycheck',
            new_name='overpaycheck',
        ),
    ]