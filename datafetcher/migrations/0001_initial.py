# Generated by Django 5.1.1 on 2024-11-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fetch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_fetched', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_fetched'],
            },
        ),
    ]
