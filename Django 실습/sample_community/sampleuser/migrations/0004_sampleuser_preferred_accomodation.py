# Generated by Django 2.2.6 on 2019-11-05 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleuser', '0003_auto_20191104_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampleuser',
            name='Preferred_Accomodation',
            field=models.CharField(default='없음', max_length=60, verbose_name='선호숙박시설'),
            preserve_default=False,
        ),
    ]
