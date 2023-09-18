# Generated by Django 4.2.5 on 2023-09-18 15:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account',
            field=models.UUIDField(default=uuid.UUID('a73f3fa0-e92c-44a2-9d70-d428bb1fc490'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_url',
            field=models.URLField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='bio',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='followers',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image_url',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
