# Generated by Django 3.2.9 on 2022-09-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]