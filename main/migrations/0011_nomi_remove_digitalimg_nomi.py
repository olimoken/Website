# Generated by Django 5.0.3 on 2024-07-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_digitalimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nomi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=80)),
            ],
        ),
        migrations.RemoveField(
            model_name='digitalimg',
            name='nomi',
        ),
    ]
