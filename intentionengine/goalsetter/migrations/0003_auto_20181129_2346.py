# Generated by Django 2.1.2 on 2018-11-29 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalsetter', '0002_inspiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goals',
            name='category',
            field=models.IntegerField(choices=[(1, 'Financial'), (2, 'Spiritual'), (3, 'Family'), (4, 'Work/Career'), (5, 'Social'), (6, 'Physical/Health'), (7, 'Mind/Intellect'), (8, 'Personal Development')], verbose_name='Category'),
        ),
    ]
