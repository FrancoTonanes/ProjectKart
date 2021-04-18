# Generated by Django 3.0 on 2021-04-18 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carreraKarting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PilotoKart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.BigIntegerField()),
                ('fecha_nacimiento', models.DateField(null=True, verbose_name='Fecha de Nacimiento(DD/MM/AAAA)')),
                ('domicilio', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.BigIntegerField(blank=True, null=True)),
                ('numero_kart', models.BigIntegerField()),
                ('categoria', models.CharField(choices=[('1', '125cc'), ('2', '150cc'), ('3', '300cc'), ('4', '350cc'), ('5', '400cc'), ('6', '500cc'), ('7', '700cc'), ('8', '710cc'), ('9', '800cc')], max_length=1)),
                ('carrera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='piloto_carrera', to='carreraKarting.CarreraKarting')),
            ],
        ),
    ]
