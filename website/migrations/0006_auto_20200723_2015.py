# Generated by Django 3.0.8 on 2020-07-23 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200723_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('google-plus', 'fa-google-plus-g'), ('rss', 'fa-rss'), ('dribble', 'fa-dribbble'), ('instagram', 'fa-instagram'), ('flickr', 'fa-flickr'), ('linkedin', 'fa-linkedin-in'), ('pinterest', 'fa-pinterest'), ('facebook', 'fa-facebook')], max_length=20, null=True),
        ),
    ]
