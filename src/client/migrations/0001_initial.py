# Generated by Django 4.1.5 on 2023-02-02 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('cin', models.CharField(max_length=12)),
                ('dateEnrg', models.DateField()),
            ],
        ),
    ]
