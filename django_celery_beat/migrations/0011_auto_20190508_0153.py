# Generated by Django 2.2 on 2019-05-08 01:53
# flake8: noqa
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0010_auto_20190429_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClockedSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clocked_time', models.DateTimeField(help_text='Run the task at clocked time', verbose_name='Clock Time')),
                ('enabled', models.BooleanField(default=True, editable=False, help_text='Set to False to disable the schedule', verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'clocked',
                'verbose_name_plural': 'clocked',
                'ordering': ['clocked_time'],
            },
        ),
        migrations.AddField(
            model_name='periodictask',
            name='clocked',
            field=models.ForeignKey(blank=True, help_text='Clocked Schedule to run the task on.  Set only one schedule type, leave the others null.', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.ClockedSchedule', verbose_name='Clocked Schedule'),
        ),
    ]
