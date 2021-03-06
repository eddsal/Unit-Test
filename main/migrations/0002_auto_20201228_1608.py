# Generated by Django 3.1 on 2020-12-28 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='listt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.list'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True, verbose_name='Email address'),
        ),
    ]
