# Generated by Django 3.2.6 on 2022-07-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0020_alter_doctors_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorcategories',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
