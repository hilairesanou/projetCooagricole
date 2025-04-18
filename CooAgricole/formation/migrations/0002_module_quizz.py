# Generated by Django 5.1.2 on 2024-10-12 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.moduleformation')),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('reponse_correcte', models.CharField(max_length=255)),
                ('choix_reponses', models.TextField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.module')),
            ],
        ),
    ]
