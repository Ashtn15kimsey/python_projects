# Generated by Django 3.2 on 2021-04-22 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('pysics', 'PHYSICS'), ('math', 'MATH'), ('world History', 'WORLD HISTORY'), ('eastern philosophy', 'EASTERN PHILOSOPHY')], max_length=100)),
                ('courseNumber', models.IntegerField(default=0)),
                ('instructorName', models.CharField(max_length=100)),
                ('duration', models.FloatField(default=0)),
            ],
        ),
    ]