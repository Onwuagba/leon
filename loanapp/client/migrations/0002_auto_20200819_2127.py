# Generated by Django 3.0.7 on 2020-08-19 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Staff'),
        ),
        migrations.AlterField(
            model_name='loans',
            name='approved_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_by', to='staff.Staff'),
        ),
        migrations.AlterField(
            model_name='loans',
            name='closed_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to='staff.Staff'),
        ),
    ]