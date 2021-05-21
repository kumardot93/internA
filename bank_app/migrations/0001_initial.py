# Generated by Django 3.2.3 on 2021-05-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=12)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=100)),
            ],
        ),
    ]