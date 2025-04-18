# Generated by Django 5.1.2 on 2024-11-15 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial'),
        ('membres', '0002_rename_telephone_membre_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='InscriptionFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.formation')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membres.membre')),
            ],
        ),
    ]
