# Generated by Django 2.1.7 on 2019-04-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floravale_bus', '0002_feedback_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='text',
            new_name='feedback',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
