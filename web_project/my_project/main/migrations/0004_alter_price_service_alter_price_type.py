# Generated by Django 5.0.3 on 2024-04-10 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_price_service_alter_price_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='service',
            field=models.CharField(choices=[('training', 'training'), ('walking', 'walking'), ('hotel', 'hotel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='price',
            name='type',
            field=models.CharField(choices=[('individual', 'individual'), ('group', 'group')], max_length=50),
        ),
    ]
