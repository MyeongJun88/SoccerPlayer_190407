# Generated by Django 2.0.13 on 2019-05-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_player2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player2',
            name='title1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
