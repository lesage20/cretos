# Generated by Django 3.0.8 on 2020-07-26 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20200725_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('prix', models.FloatField(null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('categorie_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Category_product')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
            },
        ),
    ]