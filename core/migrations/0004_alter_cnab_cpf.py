# Generated by Django 3.2.7 on 2021-09-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_cnab_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnab',
            name='cpf',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
