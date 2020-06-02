# Generated by Django 3.0.3 on 2020-05-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquationSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.DecimalField(decimal_places=12, max_digits=24)),
                ('b1', models.DecimalField(decimal_places=12, max_digits=24)),
                ('c1', models.DecimalField(decimal_places=12, max_digits=24)),
                ('a2', models.DecimalField(decimal_places=12, max_digits=24)),
                ('b2', models.DecimalField(decimal_places=12, max_digits=24)),
                ('c2', models.DecimalField(decimal_places=12, max_digits=24)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]