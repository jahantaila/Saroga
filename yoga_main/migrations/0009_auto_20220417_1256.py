# Generated by Django 3.1.6 on 2022-04-17 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga_main', '0008_yogaclass_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='yogaclass',
            name='link',
            field=models.CharField(default='Please wait 24 hours for your link to generate', max_length=50000),
        ),
        migrations.AlterField(
            model_name='yogaclass',
            name='rating',
            field=models.CharField(default='No Ratings Yet', max_length=50),
        ),
    ]
