# Generated by Django 3.2.6 on 2022-06-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0002_rename_image_patient_patientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patientImage',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
