# Generated by Django 4.1.7 on 2023-03-07 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pilot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='plane',
            name='pilots',
            field=models.ManyToManyField(to='main_app.pilot'),
        ),
    ]
