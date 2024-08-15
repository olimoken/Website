# Generated by Django 5.0.3 on 2024-07-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_nomi_remove_digitalimg_nomi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='digitalimg',
            old_name='rasm',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='digitalimg',
            name='app',
        ),
        migrations.RemoveField(
            model_name='digitalimg',
            name='imgname',
        ),
        migrations.AddField(
            model_name='digitalimg',
            name='malumot',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='digitalimg',
            name='nomi',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='digitalimg',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
