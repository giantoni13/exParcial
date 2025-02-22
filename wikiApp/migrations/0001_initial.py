# Generated by Django 4.2.16 on 2024-12-08 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temaWiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTema', models.CharField(blank=True, max_length=128, null=True)),
                ('descripcionTema', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='articuloWiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloArticulo', models.CharField(blank=True, max_length=128, null=True)),
                ('contenidoArticulo', models.CharField(blank=True, max_length=1024, null=True)),
                ('temaR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wikiApp.temawiki')),
            ],
        ),
    ]
