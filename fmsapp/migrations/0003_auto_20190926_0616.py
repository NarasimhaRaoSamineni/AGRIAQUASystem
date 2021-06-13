# Generated by Django 2.2.2 on 2019-09-26 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fmsapp', '0002_remove_user_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fmsapp.Department'),
        ),
    ]