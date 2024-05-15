# Generated by Django 3.2.25 on 2024-05-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('age', models.IntegerField(max_length=255)),
                ('account', models.DecimalField(decimal_places=2, max_digits=255)),
            ],
        ),
    ]
