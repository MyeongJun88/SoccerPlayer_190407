# Generated by Django 2.0.13 on 2019-05-05 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0011_auto_20190501_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player2',
            name='age1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player2',
            name='description1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='player2',
            name='title1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='player2',
            name='view_count1',
            field=models.IntegerField(default=0),
        ),
    ]
