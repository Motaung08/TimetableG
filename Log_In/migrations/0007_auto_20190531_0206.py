# Generated by Django 2.2 on 2019-05-31 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log_In', '0006_remove_studentsregister_cellphone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredstaffs',
            name='Course_Code',
            field=models.CharField(max_length=100),
        ),
    ]