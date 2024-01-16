# Generated by Django 4.2 on 2023-12-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='calendar',
        ),
        migrations.RemoveField(
            model_name='event',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='invitees',
            name='event',
        ),
        migrations.RemoveField(
            model_name='invitees',
            name='owner',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Calendar',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Invitees',
        ),
    ]
