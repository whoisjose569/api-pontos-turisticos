# Generated by Django 4.2.3 on 2023-07-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.CharField(max_length=150, verbose_name='Linha1')),
                ('linha2', models.CharField(blank=True, max_length=150, null=True, verbose_name='Linha2')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('pais', models.CharField(max_length=70, verbose_name='País')),
                ('latitude', models.IntegerField(blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.IntegerField(blank=True, null=True, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
