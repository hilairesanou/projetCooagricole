# Generated by Django 5.1.2 on 2024-11-15 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('adresse_livraison', models.CharField(max_length=255)),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes_commandes', to='produits.produit')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
