# Generated by Django 2.2 on 2019-04-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='fale_mais',
            field=models.TextField(blank=True, null=True),
        ),
    ]
