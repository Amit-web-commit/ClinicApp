# Generated by Django 3.2.6 on 2022-07-16 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0016_doctorcategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='categories',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clinicApp.doctorcategories'),
        ),
    ]
