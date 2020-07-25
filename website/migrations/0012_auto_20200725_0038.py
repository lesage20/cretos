# Generated by Django 3.0.8 on 2020-07-25 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20200725_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('linkedin', 'fa-linkedin-in'), ('dribble', 'fa-dribbble'), ('instagram', 'fa-instagram'), ('rss', 'fa-rss'), ('flickr', 'fa-flickr'), ('google-plus', 'fa-google-plus-g'), ('facebook', 'fa-facebook'), ('pinterest', 'fa-pinterest')], max_length=20, null=True),
        ),
    ]
