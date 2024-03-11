# Generated by Django 5.0.2 on 2024-03-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0002_rename_firsname_member_firstname'),
    ]

    operations = [
        migrations.CreateModel(
            name='StarDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surface_temperature', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
